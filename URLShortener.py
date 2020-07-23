class URL_Shortener:
      urlid = {}
      id = 1000000

      def shorten_url(self,original_url):
          if original_url in self.urlid:
             id = self.urlid[original_url]
             shorten_url = self.encode(id)
          else:
             self.urlid[original_url] = self.id
             shorten_url = self.encode(self.id)
             self.id+=1

          return "shortened_url.ly/"+str(shorten_url)           

      def encode(self, id):
          characters = "0123456789abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ" 
          base = len(characters)

          ret = []

          while id>0:
                 val = id % base
                 ret.append(characters[val])
                 id = id // base   

          return "".join(ret[::-1])      


shortener = URL_Shortener()
print(shortener.shorten_url("google.com"))
print(shortener.shorten_url("google.com"))
print(shortener.shorten_url("github.com"))
print(shortener.shorten_url("codechef.com"))
print(shortener.shorten_url("https://codeforces.com/profile/rishabh_singh_")) 