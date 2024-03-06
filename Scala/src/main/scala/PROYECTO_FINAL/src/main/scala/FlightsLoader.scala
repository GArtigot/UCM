import java.io._

object FlightsLoader extends App {

  def writeObject(flights: Seq[Flight], outputFilePath: String): Unit = {
    val out = new ObjectOutputStream(new FileOutputStream(outputFilePath))
    out.writeObject(flights)
    out.close()
  }

  val flights = ??? // TODO: carga el fichero de vuelos usando la función loadFile de FileUtils
  for (origin <- ???) { // TODO: Itera sobre los orígenes filtrados, filteredOrigin, definidos en FlightsLoaderConfig
    val filteredFligths: Seq[Flight] = ???  // TODO: Filtra los vuelos por origen
    val delayedFlights: Seq[Flight] = ??? // TODO: Filtra los vuelos retrasados por origen y ordénalos
                                          //  Pista: el atributo isDelayed de Flight te puede ayudar para realizar el filtrado
                                          //  Pista: usa la función sorted de las colecciones de Scala para ordenar
                                          //  Pista: para que la función sorted funcione, debes implementar el trait Ordered en la clase Flight
    val notDelayedFlights: Seq[Flight] = ???  // TODO: Filtra los vuelos no retrasados
                                              //  Pista: el atributo isDelayed de Flight te puede ayudar para realizar el filtrado
                                              //  Pista: usa la función sorted de las colecciones de Scala para ordenar
                                              //  Pista: para que la función sorted funcione, debes implementar el trait Ordered en la clase Flight

    val flightObjPath: String = ??? // TODO: Crea el path del fichero de salida para los vuelos no retrasados
                                    //  Pista: el path debe concatenar el directorio de salida (outputDir) con el origen
                                    //  del vuelo y la extensión .obj
    val delayedFlightsObj: String = ??? // TODO: Crea el path del fichero de salida para los vuelos retrasados
                                        //  Pista: el path debe concatenar el directorio de salida (outputDir) con el origen
                                        //  del vuelo, la cadena "_delayed" y la extensión .obj
    // TODO: Escribe los vuelos no retrasados en el fichero de salida usando la función writeObject y
    //  pasándole como parámetros los vuelos no retrasados y el path del fichero de salida para los vuelos no retrasados.
    ???
    // TODO: Escribe los vuelos retrasados en el fichero de salida usando la función writeObject y
    //  pasándole como parámetros los vuelos retrasados y el path del fichero de salida para los vuelos retrasados.
    ???
  }
}
