package org.ntic.entregable

import com.typesafe.config.{Config, ConfigFactory}

object FlightsLoaderConfig {
  /**
   * This object is used to load the configuration file -> src\main\resources\application.conf
   */
  val config: Config = ConfigFactory.load().getConfig("flightsLoader")
  val filePath: String = config.getString("filePath")
  val hasHeaders: Boolean = config.getBoolean("hasHeaders")
  val headersLength: Int = config.getStringList("headers").toArray.length
  val delimiter: String = config.getString("delimiter")
  val outputDir: String = config.getString("outputDir")
  val headers: List[String] = config.getStringList("headers").toArray.map(x => x.asInstanceOf[String]).toList
  val columnIndexMap: Map[String, Int] = headers.map(x => (x, headers.indexOf(x))).toMap
  val filteredOrigin: List[String] = config.getStringList("filteredOrigin").toArray.map(x => x.asInstanceOf[String]).toList
}
