import ejercicios_clases.scalaTrain.{Time, Train}
import ejercicios_clases.case_Time

//3.1
val train = new Train()
val train_1 = new Train(1,  "AVE")

train.numero
train_1.kind

//3.2
val time_1 = new Time(2, 2)
val time_2 = new Time(2, 4)

val c = new Time()

val minus_result = c.minus(time_1, time_2)
val operator_result = time_2 - time_1

val test_case_time = case_Time(1, 1)
val test_case_asMinutes = test_case_time.asMinutes
