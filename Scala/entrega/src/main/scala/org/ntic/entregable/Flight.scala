package org.ntic.entregable

import FlightDate.fromString

case class Flight(flDate: String,
                  origin: AirportInfo,
                  dest: AirportInfo,
                  scheduledDepTime: Time,
                  scheduledArrTime: Time,
                  depDelay: Double,
                  arrDelay: Double)  extends Ordered[Flight]{

  // Definimos el campo flightDate como perezoso e inmutable aprovechando el método fromString de flDate
  lazy val flightDate: FlightDate = fromString(flDate)

  // Definimos el campo actualDepTime como perezoso e inmutable aprovechando el método fromMinutes de Time
  // Para ello extraemos los minutos de la hora de salida y le sumamos el retraso
  // tras esto convertimos el resultado a un objeto Time con la función fromMinutes
  lazy val actualDepTime: Time = Time.fromMinutes(scheduledDepTime.hours*60 + scheduledDepTime.minutes + depDelay.toInt)

  // Repetimos la operación con la hora de llegada
  lazy val actualArrTime: Time = Time.fromMinutes(scheduledArrTime.hours*60 + scheduledArrTime.minutes + arrDelay.toInt)

  // Comprobamos si el vuelo esta retrasado o no y guardamos un variable inmutable que lo indica
  val isDelayed: Boolean = if (depDelay.toInt == 0 || arrDelay.toInt == 0) false else true

  // Implementamos el trait Ordered comparando a través de actualArrTime haciendo uso del compare ya
  // definido para la clase Tiempo, ya que es el tipo de objeto de actualArrTime
  // source: https://stackoverflow.com/questions/40886474/understanding-scala-ordered-trait-to-compare-reference
  override def compare(that: Flight): Int =
    this.actualArrTime compare that.actualArrTime
}

object Flight {

  def fromString(flightInfoRow: String): Flight = {
    val columns: Array[String] = flightInfoRow.split(FlightsLoaderConfig.delimiter)

    def getColValue(colName: String): String = {
      /**
       * This function is used to get the value of a column from the array of String generated from the row of the csv
       * and stored in the variable `columns`.
       * @param colName: String name of the column
       * @return String value of the column
       */

      // Usando columnIndexMap obtenemos el indice de entre las columna que buscamos
      // source: https://stackoverflow.com/questions/11716081/cast-optionany-to-int
      columns.apply(FlightsLoaderConfig.columnIndexMap.get(colName).get)
    }
    val oriAirport = AirportInfo(
      airportId = getColValue("ORIGIN_AIRPORT_ID").toLong,
      code = getColValue("ORIGIN"),
      cityName = getColValue("ORIGIN_CITY_NAME"),
      stateAbr = getColValue("ORIGIN_STATE_ABR"))
    val destAirport = AirportInfo(
      airportId = getColValue("DEST_AIRPORT_ID").toLong,
      code = getColValue("DEST"),
      cityName = getColValue("DEST_CITY_NAME"),
      stateAbr = getColValue("DEST_STATE_ABR"))
    Flight(
      flDate = getColValue("FL_DATE"),
      origin = oriAirport,
      dest = destAirport,
      scheduledDepTime = Time.fromString(getColValue("DEP_TIME")),
      scheduledArrTime = Time.fromString(getColValue("ARR_TIME")),
      depDelay = getColValue("DEP_DELAY").toDouble,
      arrDelay = getColValue("ARR_DELAY").toDouble
    )
  }
}
