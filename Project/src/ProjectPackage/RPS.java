package ProjectPackage;
import java.awt.*;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.util.Scanner;

public class RPS {

	static Robot r;

	public static void click(int x, int y) throws InterruptedException {
		r.mouseMove(x, y);
		Thread.sleep(50);
		r.mousePress(InputEvent.BUTTON1_MASK);
		Thread.sleep(50);
		r.mouseRelease(InputEvent.BUTTON1_MASK);
		Thread.sleep(50);
	}

	public static void main(String[] args) throws InterruptedException, AWTException {
		r = new Robot();

	}
}
