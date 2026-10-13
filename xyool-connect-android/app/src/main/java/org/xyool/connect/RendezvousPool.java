package org.xyool.connect;

import java.net.URI;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.List;

/**
 * Safe, bounded list of independent rendezvous nodes.
 *
 * Each device remains a peer; rendezvous endpoints provide reachability for
 * NAT-bound devices, not a media server and not a DHT. The first endpoint is
 * preferred. Failed connections rotate through the configured alternatives.
 */
public final class RendezvousPool {
    public static final String DEFAULT_NODE=
        "wss://xyool-id-signaling-production.up.railway.app/v1/id";
    public static final String PREF_NODES="xyool_network_bootstrap_nodes";
    private final List<URI> nodes;
    private int index=0;

    public RendezvousPool(String preferred,String extra){
        LinkedHashSet<URI> unique=new LinkedHashSet<>();
        if(preferred!=null&&!preferred.trim().isEmpty())
            unique.add(parse(preferred.trim()));
        if(extra!=null&&!extra.isEmpty()){
            if(extra.length()>2000)throw new IllegalArgumentException("Too many bootstrap entries");
            String[] parts=extra.split("[,\\r\\n]+");
            for(String part:parts){
                if(part.trim().isEmpty())continue;
                unique.add(parse(part.trim()));
                if(unique.size()>5)throw new IllegalArgumentException("Maximum five nodes");
            }
        }
        if(unique.isEmpty())unique.add(parse(DEFAULT_NODE));
        nodes=Collections.unmodifiableList(new ArrayList<>(unique));
    }
    public static URI parse(String raw){
        URI uri;
        try{uri=URI.create(raw);}catch(Exception bad){
            throw new IllegalArgumentException("Invalid WSS bootstrap URI");
        }
        if(!"wss".equalsIgnoreCase(uri.getScheme())||
           uri.getHost()==null||uri.getHost().length()>253||
           !"/v1/id".equals(uri.getPath())||uri.getUserInfo()!=null||
           uri.getQuery()!=null||uri.getFragment()!=null)
            throw new IllegalArgumentException("Bootstrap URL must be wss://host/v1/id");
        return uri;
    }
    public synchronized URI current(){return nodes.get(index);}
    public synchronized URI failover(){
        index=(index+1)%nodes.size();
        return current();
    }
    public synchronized void reset(){index=0;}
    public int count(){return nodes.size();}
    public List<URI> endpoints(){return nodes;}
}
