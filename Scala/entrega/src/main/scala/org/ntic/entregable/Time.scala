package org.ntic.entregable

case class Time(hours: Int, minutes: Int) extends Ordered[Time] {
  require(hours >= 0 && hours <= 24, f"`hours` debe estar entre 0 y 24, el valor $hours no es válido")
  require(minutes >= 0 && minutes <= 59, f"`minutes` debe estar entre 0 y 59, el valor $minutes no es válido")
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

    // Extraemos de la hora formateado las horas y minutos por separado
    val hours: Int = formatted.substring(0, 2).toInt
    val minutes: Int = formatted.substring(2).toInt

    // Definimos un objeto con las horas y minutos extraidos
    //println(hours.toString + " " + minutes.toString + " " + formatted + "\n")
    Time(hours, minutes)
  }

  def fromMinutes(minutes: Int): Time = {
    // Casuística especial en la que el retraso negativo ha hecho que se atrase un día
    // en cuyo caso la hora real serán las 23 y los minutos convenientes
    val normalized = if (minutes < 0) {
      (23 * 60 + (60 + minutes)) % totalMinutesInADay
      } else {
      minutes % totalMinutesInADay
      }

    Time(normalized / 60, normalized % 60)
  }
}