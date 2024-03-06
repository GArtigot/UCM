import com.sun.media.sound.InvalidFormatException

class FlightDateTest extends AnyFlatSpec with Matchers {
  "A FlightDate" should "be correctly initialized from string" in {
    val dateStr = "7/1/2023 12:00:00 AM"
    val expected = FlightDate(day = 7, month = 1, year = 2023)
    val result = FlightDate.fromString(dateStr)
    result shouldEqual expected
  }

  "A FlightDate" should "raise an Exception because of wrong string format" in {
    val dateStr = "7/1/2023/3 12:00:00 AM"
    an [InvalidFormatException] should be thrownBy FlightDate.fromString(dateStr)
  }
}
