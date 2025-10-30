import java.util.HashMap;
import java.util.Map;


public class BandSongList {
    public static void main(String[] args) {
        
        HashMap<String, String> trackList = new HashMap<>();
        
        trackList.put("Ocean Breeze", "Sailing through the morning light...");
        trackList.put("Sunset Dreams", "Colors fade as the night comes in...");
        trackList.put("Midnight Run", "Racing through streets, chasing stars...");
        trackList.put("Echoes of You", "Whispers linger, calling your name...");
        
        
        
        System.out.println("\n--- Track List ---");

        System.out.println("Lyrics for \"Sunset Dreams\": " + trackList.get("Sunset Dreams"));

        
        System.out.println("\n--- All Songs and Lyrics ---");
        trackList.forEach((title, lyric) -> {
            System.out.println("Title: " + title);
            System.out.println("Lyrics: " + lyric + "\n");
        });
        System.out.println();

    }
}
