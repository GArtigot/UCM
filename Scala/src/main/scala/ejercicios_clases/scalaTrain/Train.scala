package ejercicios_clases

class Train(val numero: Int, val kind: String) {

  // Constructor secundario
  def this() = {
    this(0, "no kind")
  }

}
