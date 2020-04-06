package Controller;

  public enum Message {
        SCORE_FORMAT_ERR("Средний бал студента должен быть целым или дробным положительным числом между 0 и 100"),
        OK_MESG( "ok"), 
        ACC_NUM_ERR("Номер зачетной книжки должен быть целым положительным шестизначным числом");
        String err;
        private Message (String err) {
            this.err = err;
        }
    }
