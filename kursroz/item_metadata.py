
class ItemMetadata:
    def __init__(self, title, pub_date, xml_url, pretty_html_url, ):
        self.title = title
        self.pub_date = pub_date
        self.xml_url = xml_url
        self.pretty_html_url = pretty_html_url

    def __repr__(self) -> str:
        return f"""
{type(self).__name__}(title={self.title}, 
pub_date={self.pub_date},
xml_url={self.xml_url},
pretty_html_url={self.pretty_html_url})
    """
