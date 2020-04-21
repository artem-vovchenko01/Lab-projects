public class BruteCollinearPoints {
    private Point[] points;
    private int numberOfSegments;
    private LineSegment[] segments;
    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points)
    {
        if (points == null) {
            throw new IllegalArgumentException();
        }
        this.points = points;
        LineSegment[] segs = new LineSegment[points.length * points.length];
        int pointer = 0;
        for (Point p : points) {
            for (Point q : points) {
                for (Point r : points) {
                    for (Point s : points) {
                        double sPQ = p.slopeTo(q);
                        double sPR = p.slopeTo(r);
                        double sPS = p.slopeTo(s);
                        if (p.compareTo(q) < 0 && q.compareTo(r) < 0 && r.compareTo(s) < 0) {
                            if (Double.compare(sPQ, sPR) == 0  && Double.compare(sPQ, sPS) == 0) {
                                segs[pointer++] = new LineSegment(p, s);
                            }
                        }
                    }
                }
            }

        }

        this.numberOfSegments = pointer;
        if (segs[0] == null) {
            this.segments = new LineSegment[] {};
            return;
        }
        LineSegment[] segsFinal = new LineSegment[pointer];
        for (int i = 0; i < pointer; i++) {
            segsFinal[i] = segs[i];
        }
        this.segments = segsFinal;
    }

    // the number of line segments
    public int numberOfSegments() {
        return this.numberOfSegments;
    }

    // the line segments
    public LineSegment[] segments() {
        return this.segments;
    }
}