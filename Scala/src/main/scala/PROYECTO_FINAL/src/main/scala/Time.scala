case class Time(hours: Int, minutes: Int) extends Ordered[Time] {
  require(hours >= 0 && hours <= 23, "`hours` debe estar entre 0 y 23")
  require(minutes >= 0 && minutes <= 59, "`minutes` debe estar entre 0 y 59")
  val asMinutes = hours*60 + minutes
  override lazy val toString: String = f"$hours%02d:$minutes%02d"

  def minus(that: Time): Int =
    this.asMinutes - that.asMinutes

  def -(that: Time): Int =
    minus(that)

  override def compare(that: Time): Int =
    this - that
}

object Time {

  val totalMinutesInADay = 1440
  def fromString(timeStr: String): Time = {
    val formatted: String = f"${timeStr.toInt}%04d"
    val hours: Int = ???  // TODO: Extraer las horas de la variable `formatted`, que es un String de 4 caracteres: HHMM
                          //  Pista: puedes usar el método `substring` de la clase String,
                          //    revisa el dataset para entender el formato de la variable
                          //  Pista: puedes usar el método `toInt` de la clase String
                          //  Pista: recuerda que las horas deben estar entre 0 y 23
    val minutes: Int = ???  // TODO: Extraer los minutos de la variable `formatted`, que es un String de 4 caracteres: HHMM
                            //  Pista: puedes usar el método `substring` de la clase String,
                            //    revisa el dataset para entender el formato de la variable
                            //  Pista: puedes usar el método `toInt` de la clase String
                            //  Pista: recuerda que los minutos deben estar entre 0 y 59
    ??? // TODO: Devuelve un objeto Time con las horas y minutos extraídos
  }

  def fromMinutes(minutes: Int): Time = {
    val normalized = minutes / totalMinutesInADay
    Time(normalized / 60, normalized % 60)
  }
}