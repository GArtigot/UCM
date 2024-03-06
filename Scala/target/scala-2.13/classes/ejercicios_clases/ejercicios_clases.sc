import ejercicios_clases.scalaTrain.{Time, Train}

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


val test = 0
0>3

