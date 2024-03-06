package ejercicios_clases.scalaTrain

class Time (val hours: Int, val minutes: Int) {
  val asMinutes: Int = hours * 60 + minutes

  def this() = {
    this(0 ,0)
  }

  require(hours >= 0 && hours <= 23, "hours must be between 0 and 23")
  require(minutes >= 0 && minutes <= 59, "minutes must be between 0 and 59")

  def minus(a: Time, b: Time): Int = {
    return a.asMinutes - b.asMinutes
  }

  def -(that: Time): Int = {
    return minus(this, that)
  }
}

object Time {
  def fromMinutes(minutes: Int): Time = new Time(minutes/60, minutes%60)
}