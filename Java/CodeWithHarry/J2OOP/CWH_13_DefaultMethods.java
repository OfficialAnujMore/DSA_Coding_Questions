package Java.CodeWithHarry.J2OOP;
// Interface contains static and default methods

interface Camera {
  void takeSnap();
  void recordVideo();
  default void record4KVideo(){
    System.out.println("Recording in 4K");
  }
}

interface Wifi {
  String[] getNetwork();
  void connectToNetwork(String network);
}

class cellPhone {

  void callNumber(int phoneNumber) {
    System.out.println("Calling" + phoneNumber);
  }

  void pickCall() {
    System.out.println("Connecting...");
  }
}

class SmartPhone extends cellPhone implements Camera, Wifi {

  public void takeSnap() {
    System.out.println("Taking snap");
  }


  public void record4KVideo(){
    System.out.println("Recording 4k in Smartphone");
  }

  public void recordVideo() {
    System.out.println("Recording video");
  }

  public String[] getNetwork() {
    System.out.println("Getting list of networks");
    String[] networkList = { "A1", "B1", "C2" };
    return networkList;
  }

  public void connectToNetwork(String network) {
    System.out.println("Connecting to" + network);
  }
}

class CWH_13_DefaultMethods {

  public static void main(String[] args) {
    SmartPhone sp = new SmartPhone();
    String[] ar = sp.getNetwork();
    sp.record4KVideo();

    for (String ele : ar) {
      sp.connectToNetwork(ele);
    }
  }
}
