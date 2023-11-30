package ejercicios_clases

class Time (val hours: Int, minutes: Int) {
  val asMinutes: Int = hours * 60 + minutes

  def this() = {
    this(0 ,0)
  }

  //TODO Añadir siguientes comprobaciones:
  // - hours entre 0<x<23
  // - minutes entre 0<x<59

  def minus(a: Time, b: Time): Int = {
    return a.asMinutes - b.asMinutes
  }


}
