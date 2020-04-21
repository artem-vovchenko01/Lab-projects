import java.util.Arrays;
import java.util.Comparator;

public class FastCollinearPoints {
    private class MyComparator implements Comparator<Point>
    {
        private Point src;
        public MyComparator(Point src)
        {
            this.src = src;
        }
        public int compare(Point o1, Point o2) {
            double s1 = src.slopeTo(o1);
            double s2 = src.slopeTo(o2);
            if (Double.compare(s1, s2) == 0)
                return o1.compareTo(o2);
            return s1 > s2 ? 1 : -1;
        }
    }
    private int count;
    private LineSegment[] kek;
    public FastCollinearPoints(Point[] points)  {
        LineSegment[] lines = new LineSegment[points.length*points.length];
        this.count = 0;
        Point[] ourPoints = new Point[points.length];
        for (int i = 0; i < points.length; i++) {
            ourPoints[i] = points[i];
        }
        for (Point p: ourPoints)
        {
            Arrays.sort(points, new MyComparator(p));
            for (int i = 1; i < points.length-1; i++)
            {
                if (Double.compare(p.slopeTo(points[i]), p.slopeTo(points[i+1])) == 0)
                {
                    int start = i;
                    i++;
                    while (i < points.length-1 && Double.compare(p.slopeTo(points[i]), p.slopeTo(points[i+1])) == 0)
                    {
                        i++;
                    }

                    if (i - start > 1 && p.compareTo(points[start]) < 0)
                    {
                        lines[count++] = new LineSegment(p, points[i]);
                    }
                }
            }
        }

        if (lines[0] == null)
        {
            this.kek = new LineSegment[]{};
        }
        else {
            this.kek = new LineSegment[count];
            for (int i = 0; i<count; i++)
            {
                this.kek[i] = lines[i];
            }
        }
    }
    // finds all line segments containing 4 or more points
    public           int numberOfSegments()     {
        return this.count;
    }    // the number of line segments
    public LineSegment[] segments()  {
        return this.kek;
    }              // the line segments
}
