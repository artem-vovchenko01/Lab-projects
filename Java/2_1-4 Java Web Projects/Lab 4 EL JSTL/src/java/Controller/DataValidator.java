
package Controller;

public class DataValidator {

    public static Message validateMeanScore (String score) {
        double meanScore;
            try {
                meanScore = Double.parseDouble(score);
            } catch (NumberFormatException ex) {
                return Message.SCORE_FORMAT_ERR;
            }
            if (meanScore <= 0 || meanScore > 100) {
                return Message.SCORE_FORMAT_ERR;
            }
           return Message.OK_MESG; 
   }
    
    public static Message validateAccountNumber (String accountNumber) {
           int number;
            try {
                number = Integer.parseInt(accountNumber);
            } catch (NumberFormatException ex) {
                return Message.ACC_NUM_ERR;
            }
            
            if (number < 100_000 || number > 999_999 )  {
                return Message.ACC_NUM_ERR;
            }
           return Message.OK_MESG; 
    }
    
}
