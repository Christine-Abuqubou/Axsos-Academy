package com.museum;

import java.util.ArrayList;
import java.util.Collections;

public class Museum {
    public static void main(String[] args) {

        ArrayList<Art> museum = new ArrayList<>();

        Painting p1 = new Painting("Starry Night", "Vincent van Gogh", "A night sky full of swirling stars.", "Oil");
        Painting p2 = new Painting("The Persistence of Memory", "Salvador Dali", "Melting clocks in a surreal landscape.", "Oil");
        Painting p3 = new Painting("Water Lilies", "Claude Monet", "A peaceful depiction of water lilies in a pond.", "Watercolor");

    
        Sculpture s1 = new Sculpture("David", "Michelangelo", "A masterpiece of Renaissance sculpture.", "Marble");
        Sculpture s2 = new Sculpture("The Thinker", "Auguste Rodin", "A contemplative man deep in thought.", "Bronze");

        museum.add(p1);
        museum.add(p2);
        museum.add(p3);
        museum.add(s1);
        museum.add(s2);

        Collections.shuffle(museum);

        for (Art art : museum) {
            art.viewArt();
        }
    }
}
