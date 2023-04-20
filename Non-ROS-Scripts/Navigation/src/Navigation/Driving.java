package Navigation;

public class Driving {
	
	/*Creates an array of setpoint latitude/longitudes*/
	public double[][] addSetPoint(double latitude, double longitude){
		double[][] setPoints = new double[10][10];
		return setPoints;
	}
	
	/*Returns the index of the nearest setpoint */
	public int findNearestSetpoint() {
		return 0;
	}
	
	/*Returns true if a turnNode*/
	public boolean isTurnNode() {
		return false;
	}
	
	/*Corresponds to servo angle of 3, and motor on*/
	public void driveStraight() {
		
	}
	
	/*Corresponds to a turn in servo, until next turn point is reached, motor on (maybe slower)*/
	public void turn() {
		
	}
	
	/*Corrects servo when gets off line*/
	public void correctServo() {
		
	}
}
