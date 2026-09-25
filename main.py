import argparse
import os
from openai import OpenAI
from agent import XyoolAgent, ConversationStore


def main():
    parser = argparse.ArgumentParser(description="Xyool autonomous research/development/execution agent")
    parser.add_argument("objective", nargs="*", help="objective for Xyool")
    parser.add_argument("--model", default=os.getenv("XYOOL_MODEL", "gpt-5.6-luna"))
    parser.add_argument("--chat", action="store_true")
    parser.add_argument("--session", default="default")
    parser.add_argument("--activity", choices=["human", "jsonl", "quiet"], default="human")
    parser.add_argument("--confirm-modify", action="store_true")
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required")
    if not args.chat and not args.objective:
        parser.error("provide an objective or use --chat")

    def activity(event):
        if args.activity == "quiet":
            return
        if args.activity == "jsonl":
            import json
            print(json.dumps({"ts": event.ts, "phase": event.phase, "status": event.status, "message": event.message, "detail": event.detail}))
        else:
            print(f"{'✓' if event.status == 'success' else '●'} {event.phase}: {event.message}")

    approval = (lambda kind, tool, reason: args.confirm_modify) if args.confirm_modify else None
    agent = XyoolAgent(OpenAI(), model=args.model, workspace=".", on_activity=activity, approval_callback=approval)

    if not args.chat:
        print(agent.run(" ".join(args.objective)))
        return

    session = ConversationStore(workspace=".", session_id=args.session)
    print(f"Xyool is ready. Session: {session.session_id}")
    print("Commands: /new, /clear, /history, /exit")
    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(); break
        if not user_text:
            continue
        command = user_text.lower()
        if command in {"/exit", "/quit", "exit", "quit"}: break
        if command == "/clear": session.clear(); print("Xyool: conversation cleared."); continue
        if command == "/new": session = ConversationStore.new_session(workspace="."); print(f"Xyool: new session {session.session_id}"); continue
        if command == "/history":
            history = session.load(); print(f"Xyool: {len(history)} stored message(s) in {session.session_id}.")
            for m in history[-10:]: print(f"{m['role']}: {m['content'][:500]}")
            continue
        session.append("user", user_text)
        try:
            result = agent.chat(session.load())
        except Exception as exc:
            print(f"Xyool error: {exc}"); continue
        session.append("assistant", result)
        print(f"Xyool: {result}")


if __name__ == "__main__":
    main()
