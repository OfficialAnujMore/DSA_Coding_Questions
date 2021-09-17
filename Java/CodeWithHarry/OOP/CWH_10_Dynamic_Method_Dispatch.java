// Run time poly
class Phone {

  public void canCall() {
    System.out.println("Yes can call");
  }
}

class SmartPhone extends Phone {

  public void canCall() {
    System.out.println("Yes can  smartphone call");
  }

  public void canVideoCall() {
    System.out.println("Yes can smartphone");
  }
}

class CWH_10_Dynamic_Method_Dispatch {

  public static void main(String[] args) {
    Phone obj = new SmartPhone(); // Sub method will be called
    SmartPhone obj1 = new SmartPhone();
    obj.canCall();
    obj1.canVideoCall();
  }
}
