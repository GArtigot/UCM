import sample.Time

val l = List(1, 2, 3)

l.map(n => n*n)
// x = lambda y: y*2
val fLambda = (x: Int) => x*2
l.map(fLambda)
l.map(n => n*n)
l.map(x => {
  val a = x * x
  a

})
//l.map(z => x*x)

//import sample.com.charles.scala.Ejemplo


// Any
// AnyVal(Int, Boolean, Double...) - AnyRef (List, Time)


val l2: List[Any] = List(1, 1.1, "charles", false)
val l3 = List(1, 1.1, "charles", false, List(1, 2))

l3.map(x=> x match {
  case y: Int => y*2
  case y: Double => y*2
  case y: String => y.replace(".", ",")
  case y: Boolean => if (y) 1 else 0
  case _ => "no controlado"
})

/*
def cualquierTipo(x):
  return x*x
  if:
  elif

cualquierTipo(True)

 */


val a = List(Vector(1, 2, 3), Vector(4, 5, 6)) // List[Int] = (2, 4, 6, 8, 10, 12)
// List
a.map(x => x.map( y => y*2)) // List(Vector(2, 4, 6), Vector(8, 10, 12))
//a.flatMap(x => x*2) // Vector -> *
a.flatMap(x => x.map(y => y*2)) // List(2, 4, 6, 8, 10, 12)

// Option -> Some
//        -> None


abstract class A {
  def imprime() = println("hola desde A")
  def imprimeMensaje(mensaje: String): Unit
}

class B extends A {
  override def imprime() = println("hola desde B")
  def imprimeMensaje(mensaje: String): Unit = ???
  def imprimeMensaje2(mensaje: String): Unit = ???
  def multipleTipos(): A = new B
}
class C extends B {
  override def imprime() = super.imprime()
  override def imprimeMensaje(mensaje: String): Unit = ???
  def imprimeMensaje3(mensaje: String): Unit = ???
  override def multipleTipos(): A = new C
}

// C -> B -> A
//val objA2 = new A()
val objA: A = new C // C -> A
val objA: B = new B // C -> A
//objA.imprimeMensaje("Charles")
//objA.imprime()
//objA.imprimeMensaje2()
//objA.imprimeMensaje3()
//objA.multiplesTipos




val t1 = Time(10, 15)
val t2 = Time(10, 20)

t1 > t2 // false
t1 < t2 // true

//Time.fromMinutes(1000)

val opt1: Option[String] = Some("charles")
val opt2: Option[String] = None
//val opt3: Option[String] = new Option()



val m = Map("a" -> 1, "b" -> 2)

// m["c"]
m.get("c") // m.get("c") // valor == Int, None == null
m.get("a").get // m.get("c") // valor == Int, None == null


3 / 2 // = 1.5
3.toDouble / 2
3 / 2.toDouble
3.0 / 2




 //


