package org.ntic.entregable

import java.io._
import java.nio.file.Files
import java.nio.file.Paths
import FileUtils.loadFile

object FlightsLoader extends App {

  def writeObject(flights: Seq[Flight], outputFilePath: String): Unit = {
    // source: https://stackoverflow.com/questions/28947250/create-a-directory-if-it-does-not-exist-and-then-create-the-files-in-that-direct
    if (!(Files.exists(Paths.get(outputFilePath)))){
      Files.createFile(Paths.get(outputFilePath))
    }
    val out = new ObjectOutputStream(new FileOutputStream(outputFilePath))
    out.writeObject(flights)
    out.close()
  }

  // Cargamos el fichero de vuelos
  val flights = loadFile(FlightsLoaderConfig.filePath)

  // Iteramos sobre los orgígenes filtrados
  for (origin <- FlightsLoaderConfig.filteredOrigin) {
    // Obtenemos los vuelos para este origen
    val filteredFligths: Seq[Flight] = flights.filter(_.origin.code == origin)

    // Filtramos los vuelos retrasados gracias al atributo isDelayed
    // y los ordenamos por actualArrTime gracias al trait Ordered
    val delayedFlights: Seq[Flight] = flights.filter(_.isDelayed).sorted

    // Mismo proceso anterior pero para los no retrasados
    val notDelayedFlights: Seq[Flight] = flights.filterNot(_.isDelayed).sorted

    // Creamos el path de la salida para este origen y los vuelos no retrasados
    val flightObjPath: String = FlightsLoaderConfig.outputDir + "\\" + origin + ".obj"

    // Creamos el path de la salida para este origen y los vuelos no retrasados
    val delayedFlightsObj: String = FlightsLoaderConfig.outputDir + "\\" + origin + "_delayed.obj"

    // Escribimos los vuelos no retrasados en su path correspondiente
    writeObject(notDelayedFlights, flightObjPath)

    // Escribimos los vuelos retrasados en su path correspondiente
    writeObject(delayedFlights, delayedFlightsObj)
  }
}
