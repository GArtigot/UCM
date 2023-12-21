package org.ntic.entregable

import com.sun.media.sound.InvalidFormatException
import java.time.Year

case class FlightDate(day: Int,
                      month: Int,
                      year: Int) {

  // La fecha de vuelo será lazy e inmutable de modo que solo se calcule una vez
  // source: https://stackoverflow.com/questions/3883185/use-of-lazy-val-for-caching-string-representation
  override lazy val toString = f"$day%02d/$month%02d/$year%02d"
}

object FlightDate {
  def fromString(date: String): FlightDate = {
    /**
     * This function is used to convert a string to a FlightDate
     * @param date: String
     * @return FlightDate
     */
    // Primero se comprueba que la fecha es correcta (día entre 1 y 31 segun qué mes, mes entre 1 y 12
    // y año entre 1987 y el año actual
    date.split(" ").head.split("/").map(x => x.toInt).toList match {
      case month :: day :: year :: Nil =>
          assert(year>= 1987 && year <= Year.now.getValue, "El año introducido no es válido, debe estar entre 1987 y el actual")
          assert(month >= 1 && month <= 12,"El mes introducido no es válido")
          assert(day >= 1 && day <=31, "El día del mes introducido no es válido")
          assert(((day <= 28 && month == 2) ||
            (day <= 30 && Set(4, 6, 9, 11).apply(month)) ||
            (day <= 30 && Set(1, 3, 5, 7, 8, 10, 12).apply(month))),
            "La combinación de día y mes de la fecha introducida no es válida, revísela")
          FlightDate(day, month, year)
      case _ => throw new InvalidFormatException(s"$date tiene un formato inválido")
    }
  }
}
