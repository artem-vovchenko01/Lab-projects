public class SampleClass {
    public static void main(String[] args) {
        Outer.Nested staticNested = new Outer.Nested();
        Outer outer = new Outer();
        Outer.Inner outerInner = outer.new Inner();
        outerInner.innerMethod();
        staticNested.nestedMethod();
    }
}

class Outer {
    static int staticOuterVar = 10;
    int outerVar;

    class Inner {
        int innerVar = 10;

        void innerMethod() {
            System.out.println("Inner var: " + this.innerVar);
        }
    }

    static class Nested {
        int nestedVar = 20;
         void nestedMethod() {
            int j  = Outer.staticOuterVar;
            class LocalClass {
                int i = 10;
            }
            System.out.println("Nested var : " + this.nestedVar);
            System.out.println("Static outer from nested: " + Outer.staticOuterVar);
        }
    }

    void instances() {
        StaticSorter so = new StaticSorter();
        Inner inner = new Inner();
        class Local {
            void accessFromLocal () {
                System.out.println(Outer.this.outerVar);
            }
        }
    }
}
