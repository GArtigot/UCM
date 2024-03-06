import com.typesafe.config.{Config, ConfigFactory}  // TODO: Para que esta clase funcione, debes añadir la dependencia
                                                    //  de typesafe config en build.sbt
object FlightsLoaderConfig {
  /**
   * This object is used to load the configuration file
   */
  val config: Config = ??? // TODO: Carga el fichero de configuración de la aplicación y obtén la configuración para el
                           //  objeto flightsLoader
  val filePath: String = ???  // TODO: Obtén el valor de filePath del fichero de configuración
  val hasHeaders: Boolean = ??? // TODO: Obtén el valor de hasHeaders del fichero de configuración
  val headersLength: Int = ???  // TODO: Obtén el valor de headersLength del fichero de configuración
  val delimiter: String = ??? // TODO: Obtén el valor de delimiter del fichero de configuración
  val outputDir: String = ??? // TODO: Obtén el valor de outputDir del fichero de configuración
  val headers: List[String] = config.getStringList("headers").toArray.map(x => x.asInstanceOf[String]).toList
  val columnIndexMap: Map[String, Int] = headers.map(x => (x, headers.indexOf(x))).toMap
  val filteredOrigin: List[String] = config.getStringList("filteredOrigin").toArray.map(x => x.asInstanceOf[String]).toList
}
