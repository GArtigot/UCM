package ejercicios_clases

case class case_Time(hours: Int, minutes: Int) {
  require(hours >= 0 && hours <= 23, "hours must be between 0 and 23")
  require(minutes >= 0 && minutes <= 59, "minutes must be between 0 and 59")

  val asMinutes: Int = hours * 60 + minutes
}
