Google Custom Search Python
===========================

This is a Python program to display n page Google Search results about a specific word.

# Make a Google Custom Search Engine

Go to https://www.google.com/cse/

Create a custom search engine

Get search engine ID

You can test the custom search engine by directly visiting its "Public URL" which is found in "Setup" => "Details" => "Public URL"

# Make a Google Cloud Console "Project" to get API key

Go to https://console.developers.google.com/apis/dashboard

Create a project or select

Enable APIs and services

Select Custom Search API and enable it

Click "Create credentials"

Get your credentials for Custom Search API

Go to Credentials and get API key

# CustomSearch API Client Library for Python

' $ pip install --upgrade google-api-python-client '

https://developers.google.com/api-client-library/python/apis/customsearch/v1#system-requirements

## Parameters

```
Args:
  q: string, Query (required)
  dateRestrict: string, Specifies all search results are from a time period
  hl: string, Sets the user interface language.
  orTerms: string, Provides additional search terms to check for in a document, where each document in the search results must contain at least one of the additional search terms
  highRange: string, Creates a range in form as_nlo value..as_nhi value and attempts to append it to query
  num: integer, Number of search results to return
  cr: string, Country restrict(s).
  imgType: string, Returns images of a type, which can be one of: clipart, face, lineart, news, and photo.
    Allowed values
      clipart - clipart
      face - face
      lineart - lineart
      news - news
      photo - photo
  relatedSite: string, Specifies that all search results should be pages that are related to the specified URL
  filter: string, Controls turning on or off the duplicate content filter.
    Allowed values
      0 - Turns off duplicate content filter.
      1 - Turns on duplicate content filter.
  gl: string, Geolocation of end user.
  searchType: string, Specifies the search type: image.
    Allowed values
      image - custom image search
  fileType: string, Returns images of a specified type. Some of the allowed values are: bmp, gif, png, jpg, svg, pdf, ...
  start: integer, The index of the first result to return
  imgDominantColor: string, Returns images of a specific dominant color: yellow, green, teal, blue, purple, pink, white, gray, black and brown.
    Allowed values
      black - black
      blue - blue
      brown - brown
      gray - gray
      green - green
      pink - pink
      purple - purple
      teal - teal
      white - white
      yellow - yellow
  lr: string, The language restriction for the search results
    Allowed values
      lang_ar - Arabic
      lang_bg - Bulgarian
      lang_ca - Catalan
      lang_cs - Czech
      lang_da - Danish
      lang_de - German
      lang_el - Greek
      lang_en - English
      lang_es - Spanish
      lang_et - Estonian
      lang_fi - Finnish
      lang_fr - French
      lang_hr - Croatian
      lang_hu - Hungarian
      lang_id - Indonesian
      lang_is - Icelandic
      lang_it - Italian
      lang_iw - Hebrew
      lang_ja - Japanese
      lang_ko - Korean
      lang_lt - Lithuanian
      lang_lv - Latvian
      lang_nl - Dutch
      lang_no - Norwegian
      lang_pl - Polish
      lang_pt - Portuguese
      lang_ro - Romanian
      lang_ru - Russian
      lang_sk - Slovak
      lang_sl - Slovenian
      lang_sr - Serbian
      lang_sv - Swedish
      lang_tr - Turkish
      lang_zh-CN - Chinese (Simplified)
      lang_zh-TW - Chinese (Traditional)
  siteSearch: string, Specifies all search results should be pages from a given site
  cref: string, The URL of a linked custom search engine
  sort: string, The sort expression to apply to the results
  hq: string, Appends the extra query terms to the query.
  c2coff: string, Turns off the translation between zh-CN and zh-TW.
  googlehost: string, The local Google domain to use to perform the search.
  safe: string, Search safety level
    Allowed values
      high - Enables highest level of safe search filtering.
      medium - Enables moderate safe search filtering.
      off - Disables safe search filtering.
  exactTerms: string, Identifies a phrase that all documents in the search results must contain
  lowRange: string, Creates a range in form as_nlo value..as_nhi value and attempts to append it to query
  imgSize: string, Returns images of a specified size, where size can be one of: icon, small, medium, large, xlarge, xxlarge, and huge.
    Allowed values
      huge - huge
      icon - icon
      large - large
      medium - medium
      small - small
      xlarge - xlarge
      xxlarge - xxlarge
  imgColorType: string, Returns black and white, grayscale, or color images: mono, gray, and color.
    Allowed values
      color - color
      gray - gray
      mono - mono
  rights: string, Filters based on licensing. Supported values include: cc_publicdomain, cc_attribute, cc_sharealike, cc_noncommercial, cc_nonderived and combinations of these.
  excludeTerms: string, Identifies a word or phrase that should not appear in any documents in the search results
  linkSite: string, Specifies that all search results should contain a link to a particular URL
  cx: string, The custom search engine ID to scope this search query
  siteSearchFilter: string, Controls whether to include or exclude results from the site named in the as_sitesearch parameter
    Allowed values
      e - exclude
      i - include
```
