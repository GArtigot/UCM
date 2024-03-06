package ejercicios_clases.scalaTrain

class Train(val numero: Int, val kind: String, val schedule: Seq[Station]) {

  // Constructor secundario
  def this() = {
    this(0, "no kind", Seq( new Station("none")))
  }

}
