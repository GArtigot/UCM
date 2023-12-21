import sbtassembly.AssemblyPlugin.defaultShellScript

ThisBuild / version := "0.1.0-SNAPSHOT"
ThisBuild / scalaVersion := "2.13.12"
ThisBuild / assemblyPrependShellScript := Some(defaultShellScript)


val mainClassName = "org.ntic.entregable.FlightsLoader"


lazy val root = (project in file("."))
  .settings(
    name := "entregable", // Nombre del proyecto
    Compile / run / mainClass := Some("org.ntic.entregable.FlightsLoader"), // Clase principal para la tarea run
    Compile / packageBin / mainClass := Some("org.ntic.entregable.FlightsLoader"), // Clase principal para la etapa packageBin de compile
    assembly / mainClass := Some("org.ntic.entregable.FlightsLoader"), // Clase principal para la tarea assembly
    assembly / assemblyJarName := "flights_loader.jar", // Nombre `flights_loader.jar` para el jar que se genera en la etapa assembly

    libraryDependencies ++= Seq(
      "com.typesafe" % "config" % "1.4.3",
      "org.scalatest" %% "scalatest" % "3.2.17" % Test,
      "org.scala-lang" %% "toolkit-test" % "0.1.7" % Test
    )
  )
