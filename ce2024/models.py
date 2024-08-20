from django.db import models
from datetime import datetime


#Django Rest Framework (DRF): Se você precisa expor esses dados via API.
#Django GeoDjango: Para trabalhar com dados geoespaciais mais complexos, como mapas e regiões.

class PlanoDeGoverno(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo

class Proposta(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo

class Acao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_realizacao = models.DateField()
    
    def __str__(self):
        return self.titulo


class Equipe(models.Model):
    id   = models.AutoField(primary_key=True)    
    nome = models.CharField(max_length=100)       
    celular = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    # Funcao
    funcao_opcoes = [
        ('Gerente', 'Gerente'),        
        ('Cordenador', 'Cordenador'),
        ('Colaborador', 'Colaborador'),
        ('Cabo Eleitoral', 'Cabo Eleitoral'),        
        ('Administrativo', 'Administrativo'),                
        ('Auxiliar', 'Auxiliar'), 
        ('Evangelista', 'Evangelista'),                                               
    ]
    funcao   = models.CharField(max_length=20, choices=funcao_opcoes)            
    tipo_opcoes = [
        ('Interna', 'Interna'),        
        ('Externa', 'Externa'),
        ('Ambos', 'Ambos'),
    ]    
    tipo   = models.CharField(max_length=20, choices=tipo_opcoes)        
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
 
    def __str__(self):
        return self.nome


class Municipio(models.Model):
    id   = models.AutoField(primary_key=True)        
    ibge = models.PositiveIntegerField()    
    nome = models.CharField(max_length=100)
    estado_opcoes = [
            ('GO', 'GOIAS'),        
            ('DF', 'DISTRITO FEDERAL'),            
        ]        
    estado = models.CharField(max_length=20, choices=estado_opcoes)        
    populacao = models.IntegerField()
    area_km2 = models.DecimalField(max_digits=10, decimal_places=3,default=0)    
    densidade_demografica=models.DecimalField(max_digits=10, decimal_places=2,default=0)    
    idhm=models.DecimalField(max_digits=10, decimal_places=4,default=0)    
    receita_realizada=models.DecimalField(max_digits=12, decimal_places=2,default=0)        
    despesa_realizada=models.DecimalField(max_digits=12, decimal_places=2,default=0)            
    pib_percapita=models.DecimalField(max_digits=12, decimal_places=2,default=0)    

    def __str__(self):
        return f"{self.nome} - {self.estado}"
    
    
class Regiao(models.Model):
    id   = models.AutoField(primary_key=True)            
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='regioes')
    regional = models.IntegerField()                    
    populacao = models.IntegerField()
    area_km2 = models.DecimalField(max_digits=10, decimal_places=2)    
    habitacoes = models.IntegerField()    
    familias = models.IntegerField()      
    bairros = models.IntegerField()                
    
    classe_opcoes = [
        ('Alta', 'Alta'),        
        ('Media', 'Media'),
        ('Baixa', 'Baixa'),
        ('Entusiasta', 'Entusiasta'),                
    ]          
    classe = models.CharField(max_length=15, choices=classe_opcoes) 

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome    
    

   
class Bairro(models.Model):
    id   = models.AutoField(primary_key=True)            
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio')
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='regiao')    
    populacao = models.IntegerField(default=0)
    area_km2 = models.DecimalField(max_digits=10, decimal_places=2,default=0)    
    habitacoes = models.IntegerField(default=0)    
    familias = models.IntegerField(default=0)      
    quantidade_ruas = models.IntegerField(default=0)                
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)            
    classe_opcoes = [
        ('Alta', 'Alta'),        
        ('Media', 'Media'),
        ('Baixa', 'Baixa'),
        ('Entusiasta', 'Entusiasta'),                
    ]          
    classe = models.CharField(max_length=15, choices=classe_opcoes,default='Media')    

    def __str__(self):
        return self.nome        
    
class ZonaEleitoral(models.Model):
    id   = models.AutoField(primary_key=True)                
    codigo = models.CharField(max_length=50)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='zonas_eleitorais')
    descricao = models.TextField()

    def __str__(self):
        return self.codigo    
    
class Eleitor(models.Model):
    id   = models.AutoField(primary_key=True)                    
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='eleitores')
    zona_eleitoral = models.ForeignKey(ZonaEleitoral, on_delete=models.CASCADE, related_name='eleitores', null=True, blank=True)
    # Endereço
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()    
    contato = models.CharField(max_length=100)
    perfil_opcoes = [
        ('Apoiador', 'Apoiador'),        
        ('Indeciso', 'Indeciso'),
        ('Opositor', 'Opositor'),
        ('Entusiasta', 'Entusiasta'),        
        ('Colaborador', 'Colaborador'),              
    ]          
    perfil_eleitoral = models.CharField(max_length=15, choices=perfil_opcoes)    
    celular = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    # Redes Sociais
    instagram = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    tiktok = models.URLField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.nome_completo    

class AtividadeCampanha(models.Model):
    id   = models.AutoField(primary_key=True)            
    tipo_atividade = [
        ('COM', 'Comício'),
        ('PAN', 'Panfletagem'),
        ('CAR', 'Carreata'),        
        ('VIS', 'Visita Domiciliar'),
        ('COR', 'Visita Corporativa'),        
        ('REU', 'Reuniao Politica'),        
        ('PUB', 'Evento Publico'),                
        ('PRI', 'Evento Privado'),                        
        # outros tipos de atividade
    ]
    tipo = models.CharField(max_length=3, choices=tipo_atividade)

    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='atividade')
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name='atividade')    
    data_hora = models.DateTimeField()
    descricao = models.TextField()
    numero_participantes = models.IntegerField()
    agendado_por = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='atividade')    
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.get_tipo_display()} em {self.regiao} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"



class CampanhaEleitoral(models.Model):
    id   = models.AutoField(primary_key=True)    
    nome = models.CharField(max_length=100)    
    nome_registro = models.CharField(max_length=100)        
    celular = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    # Endereço
    cep = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=100)
    latitude = models.FloatField()    
    longitude = models.FloatField()        
        
    # Cargo Candidato
    candidato_opcoes = [
        ('V', 'Vereador'),
        ('P', 'Prefeito'),
    ]
    candidato   = models.CharField(max_length=15, choices=candidato_opcoes)    

    # Partido Candidato
    partido_opcoes = [
        ('UB', 'UB'),
        ('PMDB', 'PMDB'),
        ('PSDB', 'PSDB'),                
        ('PL', 'PL'),                
        ('PT', 'PT'),        
    ]    
    partido     = models.CharField(max_length=15, choices=partido_opcoes)    

    numero      = models.PositiveIntegerField(default=0)    
    data_inicio = models.DateField()
    data_fim    = models.DateField()
    ativo      = models.BooleanField(default=True)    

    # Redes Sociais
    instagram = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    tiktok = models.URLField(max_length=255, blank=True, null=True)

    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['nome']
 
    def __str__(self):
        return self.nome
    

class LocalArmazenamento(models.Model):
    id   = models.AutoField(primary_key=True)           
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    ativo      = models.BooleanField(default=True)    
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome
    
class MaterialCampanha(models.Model):
    id   = models.AutoField(primary_key=True)               
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

   # Partido Candidato
    tipo_opcoes = [
        ('Planfeto', 'Planfleto'),
        ('Adesivo', 'Adesivo'),
        ('Sitru', 'Sitru'),        
        ('Banner', 'Banner'),                
        ('Brinde', 'Brinde'),                
        ('Santinho', 'Santinho'),        
        ('Santinho casado', 'Santinho Casado'),                
    ]    
    tipo = models.CharField(max_length=30, choices=tipo_opcoes)
    campanha = models.ForeignKey(CampanhaEleitoral, on_delete=models.CASCADE)
    ativo      = models.BooleanField(default=True)        
    
    def __str__(self):
        return f"{self.nome} ({self.campanha.nome})"   
    
class Estoque(models.Model):
    id   = models.AutoField(primary_key=True)                   
    material = models.ForeignKey(MaterialCampanha, on_delete=models.CASCADE)
    local = models.ForeignKey(LocalArmazenamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)



    class Meta:
        unique_together = ('material', 'local')

    def __str__(self):
        return f"{self.material.nome} - {self.local.nome} ({self.quantidade})"
    
class MovimentacaoMaterial(models.Model):
    id   = models.AutoField(primary_key=True)               
    material = models.ForeignKey(MaterialCampanha, on_delete=models.CASCADE)
    local_origem = models.ForeignKey(LocalArmazenamento, related_name='origem', on_delete=models.CASCADE)
    local_destino = models.ForeignKey(LocalArmazenamento, related_name='destino', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantidade} unidades de {self.material.nome} de {self.local_origem.nome} para {self.local_destino.nome} em {self.data_movimentacao}"
    
class SolicitacaoMaterial(models.Model):
    material = models.ForeignKey(MaterialCampanha, on_delete=models.CASCADE)
    quantidade_solicitada = models.PositiveIntegerField()
    quantidade_aprovada = models.PositiveIntegerField(null=True, blank=True)
    local_entrega = models.ForeignKey(LocalArmazenamento, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Negada', 'Negada'),
        ('Entregue', 'Entregue'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solicitação de {self.quantidade_solicitada} unidades de {self.material.nome} por {self.solicitante.username}"
       
    
class AplicacaoMaterial(models.Model):
    id   = models.AutoField(primary_key=True)               
    material = models.ForeignKey(MaterialCampanha, on_delete=models.CASCADE)
    local_opcoes = [
        ('Comite', 'Comite'),
        ('Pre-Posto', 'Pre-posto'),
        ('Acao', 'Acao'),
        ('Externo', 'Externo'),
    ]
    local_aplicacao = models.CharField(max_length=10, choices=local_opcoes, default='Comite')
    quantidade = models.PositiveIntegerField()
    descricao = models.CharField(max_length=200) 
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    foto_aplicao = models.ImageField(upload_to='acao_fotos/', blank=True, null=True)
    criado        = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantidade} unidades de {self.material.nome} no {self.local_aplicacao} em {self.data_movimentacao}"
   