ThisBuild / version := "0.1.0-SNAPSHOT"
ThisBuild / scalaVersion := "2.13.12"
ThisBuild / assemblyPrependShellScript := Some(defaultShellScript)


val mainClassName = "org.ntic.entregable.FlightsLoader"


lazy val root = (project in file("."))
  .settings(
    name := "", // TODO: establece el nombre del proyecto. Tiene que ser el mismo que el nombre que le has dado al proyecto en IntelliJ
    // TODO: define la clase principal del proyecto para la etapa `run` de `Compile`
    // TODO: define la clase principal del proyecto para la etapa `packageBin` de `Compile`
    // TODO: define la clase principal del proyecto para el ensamblado de `assembly`
    // TODO: define `flights_loader.jar` como el nombre del jar que se genera en la etapa assembly

    libraryDependencies ++= Seq(
      // TODO añade la dependencia de la librería de configuración de Typesafe
      "org.scalatest" %% "scalatest" % "3.2.17" % Test,
      "org.scala-lang" %% "toolkit-test" % "0.1.7" % Test
    )
  )
