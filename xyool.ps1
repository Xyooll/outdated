# Start the Xyool interactive agent from the repository root.
if (Test-Path .\.venv\Scripts\python.exe) {
    & .\.venv\Scripts\python.exe operation-dna\xyool.py @args
} else {
    python operation-dna\xyool.py @args
}
