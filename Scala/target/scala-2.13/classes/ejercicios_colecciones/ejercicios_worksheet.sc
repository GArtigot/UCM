//1. Escribir en Scala el código equivalente a:
//for (int i=10; i>=0; i--) println(i)

val l = 0 to 10
println(l mkString ",") //-->Convirtiendo en String
l.foreach(println) //--> Mejor forma
for(element<-l){  //--> Bucle clasico
  println(element)
}

//2. Definir una función cuya firma es: countDown(n: Int): Unit. Esta función
//imprimirá los números de n a 0

def countDown(n: Int): Unit = {
  val n_to_0 = n to 0
  n_to_0.foreach(println)
}

countDown(5)

//3. Escribir el código que asigne a la variable 'a' una colección (da igual si se
//define para, Seq, List, Array) de n enteros aleatorios entre 0 (incluído) y n
//(excluido)

def createRandomList(upper_limit: Int): List[Int] = {
  return ((0 to upper_limit).map(_ => (scala.util.Random.nextInt(upper_limit-1)))).toList
}
var a = createRandomList(5)

//4. Dado una colección de enteros, se pide generar una nueva colección que
//contenga todos los números positivos de la colección original en el orden de la
//primera colección seguidos por los ceros y negativos, todos en su orden
//original

val a_pos = a.filter(n => n > 0)
val a_zeros = a.filter(n => n == 0)
val a_neg = a.filter(n => n < 0)

val new_a = a_pos:::a_zeros:::a_neg

//5. Definir una función que calcule la media de un Array[Double]

def arrayAvg(n: Array[Double]): Double = {
  return n.reduce((a, b) => a + b)/n.length
}

val test_5 = arrayAvg(Array(2.7, 5.4, 6.9))

//6. Definir una función que reciba un argumento de tipo Array[Int] y devuelva un
//Array[Int] sin duplicados.

def noDups(n: Array[Int]): Array[Int] = {
  val n_set = n.toSet
  return n_set.toArray
}
val xx = Array(7, 5, 5, 5, 6)
val zz = noDups(xx)

//7. Definir una función que reciba un argumento de tipo Seq[Int] y devuelva otra
//secuencia sin ceros.

def noZeros(n: Seq[Int]): Seq[Int] = {
  return n.filter(n => n!=0)
}

val aa = Seq(1, 5, 0, 0, 4)
val ss = noZeros(aa)

//8. Definir una función que reciba un argumento de tipo Map[String, Int] y produzca
//un Map[String, Int] manteniendo las mismas claves, pero con los valores
//incrementados en 100.

//def valuesPlus100(n: Map[String, Int]): scala.collection.mutable.Map[String, Int] = {
//  val n_plus_100 = scala.collection.mutable.Map[String, Int]()
//  val n_plus_100 ++= n
//
//  //for(key<-n_plus_100.keys) {
//  //  n_plus_100(key) = n(key)+100
//  //}
//  return n_plus_100
//}
//val dd = Map("a" -> 1, "b" ->2)
//
//val cc = valuesPlus100(dd)

// 9.Definir una función que reciba una colección: minmax(values: Array[Int]) que
//devuelva un par (tupla) con el menor y mayor valor del array.

def minmax(values: Array[Int]): Tuple2[Int, Int] = {
  val max = values.reduceLeft(_ max _)
  val min = values.reduceLeft(_ min _)
  return Tuple2(min,max)
}

val test_9 = Array(0, 1, 2, 3, 4)

val return_min_max = minmax(test_9)

//10. Definir una función que reciba como argumento un String y produzca un mapa
//con los índices de todos los carácteres. Por ejemplo: Si recibe "albacete", se
//produzca un mapa: Map("a"->[0, 3], "l"->[1], "b"->[2] ...)

val val_10 = "aabcde"


val list_10 = val_10.toList

val_10.indexOf("a")

