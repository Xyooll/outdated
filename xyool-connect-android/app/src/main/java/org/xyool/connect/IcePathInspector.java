package org.xyool.connect;

import java.util.Locale;

/**
 * Sanitized ICE observations for diagnostics; does NOT send IP addresses,
 * WebRTC SDP, account identifiers or server credentials to a telemetry backend.
 *
 * ICE candidate lines may reveal network addresses; only counts/types are kept.
 * Candidate presence is NOT proof of an established connection.
 */
public final class IcePathInspector {
    private int host, srflx, prflx, relay, unknown, ipv6;
    private String iceState = "NEW";
    private String discovery = "Not evaluated";

    public synchronized void record(String candidate) {
        if (candidate == null || candidate.length() > 4096) return;
        String s = candidate.trim();
        if (!s.startsWith("candidate:")) return;
        String[] fields = s.split("\\s+");
        String type = "";
        for (int i = 0; i + 1 < fields.length; i++) {
            if ("typ".equals(fields[i])) {
                type = fields[i + 1].toLowerCase(Locale.US);
                break;
            }
        }
        if ("host".equals(type)) host++;
        else if ("srflx".equals(type)) srflx++;
        else if ("prflx".equals(type)) prflx++;
        else if ("relay".equals(type)) relay++;
        else unknown++;

        // Component ID, protocol, priority, address, port, typ, candidate type.
        if (fields.length > 4 && fields[4].indexOf(':') != -1) ipv6++;
    }

    public synchronized void setState(String state) {
        if (state == null || !state.matches("^[A-Z_]{2,30}$")) return;
        iceState = state;
    }

    public synchronized void setDiscovery(String value) {
        if (value == null || value.length() > 90) return;
        discovery = value;
    }

    public synchronized boolean hasServerReflexiveCandidates() {
        return srflx > 0;
    }

    public synchronized String summary() {
        return "ICE state: " + iceState +
            "\nCandidates: local " + host +
            " / STUN " + srflx +
            " / peer-reflexive " + prflx +
            " / relay " + relay +
            " / other " + unknown +
            "\nIPv6 candidates: " + ipv6 +
            "\nSignaling: " + discovery;
    }

    public synchronized String interpretation() {
        if ("CONNECTED".equals(iceState) || "COMPLETED".equals(iceState))
            return "A WebRTC candidate pair connected. This alone does not " +
                "identify which network path won.";
        if ("FAILED".equals(iceState)) {
            if (host == 0 && srflx == 0 && relay == 0)
                return "No usable local ICE candidates appeared. Check app network access.";
            if (srflx == 0 && relay == 0)
                return "Only local network candidates were found; STUN, IPv6 " +
                    "reachability and network restrictions need investigation.";
            return "Candidate discovery succeeded, but ICE connectivity checks " +
                "failed. A router, firewall or carrier NAT may block direct media.";
        }
        if ("CHECKING".equals(iceState))
            return "Testing candidate pairs. Discovery does not guarantee a route.";
        return "No failed or successful ICE connection is established yet.";
    }
}
