/PROG  ROS
/ATTR
OWNER		= MNEDITOR;
COMMENT		= "r2";
PROG_SIZE	= 176;
CREATE		= DATE 12-10-02  TIME 12:08:46;
MODIFIED	= DATE 12-10-02  TIME 12:08:46;
FILE_NAME	= ;
VERSION		= 0;
LINE_COUNT	= 3;
MEMORY_SIZE	= 556;
PROTECT		= READ_WRITE;
TCD:  STACK_SIZE	= 0,
      TASK_PRIORITY	= 50,
      TIME_SLICE	= 0,
      BUSY_LAMP_OFF	= 0,
      ABORT_REQUEST	= 0,
      PAUSE_REQUEST	= 7;
DEFAULT_GROUP	= *,*,*,*,*;
CONTROL_CODE	= 00000000 00000000;
/MN
   1:  RUN ROS_STATE ;
   2:  RUN ROS_MOVESM ;
   3:  CALL ROS_RELAY    ;
/POS
/END
