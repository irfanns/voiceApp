import std/[httpclient, json], nimpy

proc translate_text*(oText: string): string {.exportpy.} =
  let client = newHttpClient()
  client.headers = newHttpHeaders({"Content-Type": "application/json"})
  let body = %*{
    "q": oText,
    "source": "en",
    "target": "ja",
    "format": "text",
  }
  let response = client.request("http://localhost:5000/translate",
      httpMethod = HttpPost, body = $body)

  let resp_data = parseJson response.body
  let text = resp_data{"translatedText"}.getStr() # overloading, {} return nil JsonNode instead of error if field doesn't exit/initialized. Thank you @Yardanico!
  if text != "":
    return text
