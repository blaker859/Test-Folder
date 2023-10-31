class HelloWorld {
    public static void main(String[] args) {

        int digits = 5;
        double decimal = 1;
        for (int i = 0; i < digits; i++) {
            decimal = decimal / 10;
        }

        System.out.println(decimal);

        double shares = 526000;

        shares = shares * decimal;

        System.out.println(shares);

    }
}