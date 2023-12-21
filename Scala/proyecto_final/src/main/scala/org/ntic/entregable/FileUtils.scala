package org.ntic.entregable

import scala.io.Source

object FileUtils {

  def isInvalid(s: String): Boolean = {
    /**
     * This function is used to check if the line is valid or not
     * @param s: String
     * @return Boolean: true if the line is invalid, false otherwise
     */
    // Separamos la linea por el delimitador ";"
    val split_line = s.split(FlightsLoaderConfig.delimiter)

    // Comprobamos si no está vacia o si tiene elementos vacios, en cuyo caso sería inválida
    if (split_line.isEmpty || split_line.length != FlightsLoaderConfig.headersLength){
      true
    }
    else {
      false
    }

  }

  def loadFile(filePath: String): Seq[Flight] = {
    /**
     * This function is used to load the file
     * @param filePath: String
     * @return Seq[Flight]
     */
    //Obtener datos y cabecera del CSV por separado
    val buffer = Source.fromFile(filePath)
    val linesList: List[String] = buffer.getLines().toList
    val headers = linesList.head

    // Comprobamos que el número de cabeceras extraídas es el mismo que el definido en el archivo de configuración
    require(headers.split(FlightsLoaderConfig.delimiter).length == FlightsLoaderConfig.headersLength)

    // Extraemos sólo las filas con datos
    val rows = linesList.tail

    // Extraemos las filas válidas e inválidas por separado
    val invalidRows: List[String] = rows.filter(isInvalid(_) == true)
    val validRows: List[String] = rows.filter(isInvalid(_) == false)

    // Las filas válidas son mapeadas como objetos Flight
    val flights: Seq[Flight] = validRows.map(Flight.fromString)

    // Se devuelven los objetos Flight
    flights
  }

}