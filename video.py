import web
from web import form
from data import cliente
from data import peliculas
render=web.template.render('templates')
urls = (
    '/(.*)', 'index'
)

db = web.database(dbn='mysql', db='ncweet07c58ney5j', user='y74zq2bojb0c2jmi', pw='u1b4adeyi6vmpbyd', host="o61qijqeuqnj9chh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com")

cliente = cliente()  
cliente.read()
peliculas=peliculas()
peliculas.read()
myform = form.Form( 
    form.Dropdown('Cliente', cliente.getCliente()), 
    form.Dropdown('Pelicula',peliculas.getPelicula()), 
    form.Dropdown('Formato', ["BLUERAY","DVD"]),
     form.Dropdown('Tiempo', ["1","2","3","4","5","6","7","8","9","10"])
    
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        result=db.select('movies')
        return render.index(form,result)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            costo=0
            if form.d.Formato=="BLUERAY":
                costo=20
            elif form.d.Formato=="DVD":
                costo=10
            total=int(form.d.Tiempo)*costo
            db.insert('movies',pelicula=form.d.Pelicula, formato=form.d.Formato,cliente=form.d.Cliente, tiempo=form.d.Tiempo,total=total)
            
            result=db.select('movies')
            return render.index(form,result)
    

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
