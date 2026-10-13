package org.xyool.connect;

import android.content.Context;
import android.content.SharedPreferences;
import org.json.JSONArray;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

/**
 * User-owned, app-private Xyool ID contacts. Names and IDs are stored locally;
 * QR device-key pins remain separately managed by PhoneIdentity.
 * Unverified typed IDs are never promoted to verified identities.
 */
public final class SavedContacts {
    private static final String PREF_CONTACTS="xyool_saved_contacts_v1";
    private static final int LIMIT=250;
    private static final String ID_REGEX="^XY-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}-[A-HJ-NP-Z2-9]{4}$";
    private final SharedPreferences prefs;

    public static final class Entry {
        public final String id;
        public final String name;
        Entry(String id,String name){this.id=id;this.name=name;}
    }

    public SavedContacts(Context context){
        prefs=context.getSharedPreferences("xyool_private",Context.MODE_PRIVATE);
    }
    public static boolean validId(String id){
        return id!=null && id.matches(ID_REGEX);
    }
    public static String safeName(String raw,String id){
        String name=raw==null?"":raw.replaceAll("[\\p{Cntrl}]", " ").trim();
        if(name.length()>48)name=name.substring(0,48).trim();
        return name.isEmpty()?id:name;
    }
    public synchronized List<Entry> all(){
        ArrayList<Entry> result=new ArrayList<>();
        try{
            JSONArray arr=new JSONArray(prefs.getString(PREF_CONTACTS,"[]"));
            for(int i=0;i<arr.length()&&result.size()<LIMIT;i++){
                JSONObject o=arr.optJSONObject(i);
                if(o==null)continue;
                String id=o.optString("id","");
                if(!validId(id))continue;
                boolean duplicate=false;
                for(Entry old:result)if(old.id.equals(id)){duplicate=true;break;}
                if(!duplicate)result.add(new Entry(id,safeName(o.optString("name",""),id)));
            }
        }catch(Exception ignored){} // Malformed data must never invent a contact.
        return result;
    }
    public synchronized boolean save(String id,String name){
        if(!validId(id))return false;
        List<Entry> contacts=all();
        boolean found=false;
        for(int i=0;i<contacts.size();i++){
            if(contacts.get(i).id.equals(id)){
                contacts.set(i,new Entry(id,safeName(name,id)));found=true;break;
            }
        }
        if(!found){
            if(contacts.size()>=LIMIT)return false;
            contacts.add(new Entry(id,safeName(name,id)));
        }
        return write(contacts);
    }
    public synchronized boolean remove(String id){
        if(!validId(id))return false;
        List<Entry> contacts=all();
        if(!contacts.removeIf(entry->entry.id.equals(id)))return false;
        return write(contacts);
    }
    private boolean write(List<Entry> entries){
        JSONArray arr=new JSONArray();
        try{
            for(Entry entry:entries){
                JSONObject o=new JSONObject();
                o.put("id",entry.id);o.put("name",entry.name);
                arr.put(o);
            }
            // Commit before returning so rapid app closure does not lose a scan.
            return prefs.edit().putString(PREF_CONTACTS,arr.toString()).commit();
        }catch(Exception ignored){return false;}
    }
}
