#Boa:Frame:Frame1

import wx
import sys
import Esteganografia

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNOCULTAR, wxID_FRAME1BTNOCULTARLIMPAR, 
 wxID_FRAME1BTNOCULTARPROCURAR, wxID_FRAME1BTNOCULTARSAIR, 
 wxID_FRAME1BTNRECUPERAR, wxID_FRAME1BTNRECUPERARLIMPAR, 
 wxID_FRAME1BTNRECUPERARPROCURAR, wxID_FRAME1BTNRECUPERARSAIR, 
 wxID_FRAME1GGOCULTAR, wxID_FRAME1GGRECUPERAR, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1RBOCULTARNAO, 
 wxID_FRAME1RDOCULTARSIM, wxID_FRAME1RDRECUPERARNAO, 
 wxID_FRAME1RDRECUPERARSIM, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICBOX4, wxID_FRAME1STATICBOX5, 
 wxID_FRAME1STATICBOX6, wxID_FRAME1STATICTEXT1, wxID_FRAME1TXTARQUIVOOCULTAR, 
 wxID_FRAME1TXTARQUIVORECUPERAR, wxID_FRAME1TXTOCULTARCHAVE, 
 wxID_FRAME1TXTOCULTARMSG, wxID_FRAME1TXTRECUPERARCHAVE, 
 wxID_FRAME1TXTRECUPERARMSG, 
] = [wx.NewId() for _init_ctrls in range(31)]

class Frame1(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'Hide')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text=u'Extract')
        parent.AddPage(imageId=-1, page=self.staticText1, select=False,
              text=u'About')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(457, 234), size=wx.Size(553, 511),
              style=wx.DEFAULT_FRAME_STYLE, title='Steganography')
        self.Show(True)
        self.SetClientSize(wx.Size(545, 484))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(545, 484), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Steganography 0.1v - Python, wxPython', name='staticText1', parent=self.notebook1,
              pos=wx.Point(0, 0), size=wx.Size(537, 458), style=0)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(537, 458),
              style=wx.TAB_TRAVERSAL)

        self.txtOcultarMsg = wx.TextCtrl(id=wxID_FRAME1TXTOCULTARMSG,
              name=u'txtOcultarMsg', parent=self.panel1, pos=wx.Point(8, 16),
              size=wx.Size(280, 368), style=wx.VSCROLL | wx.TE_MULTILINE,
              value=u'')

        self.btnOcultarSair = wx.Button(id=wxID_FRAME1BTNOCULTARSAIR,
              label=u'Quit', name=u'btnOcultarSair', parent=self.panel1,
              pos=wx.Point(392, 408), size=wx.Size(120, 32), style=0)
        self.btnOcultarSair.Bind(wx.EVT_BUTTON,
              self.OnBtnOcultarSair, id=wxID_FRAME1BTNOCULTARSAIR)

        self.btnOcultar = wx.Button(id=wxID_FRAME1BTNOCULTAR, label=u'Hide message!',
              name=u'btnOcultar', parent=self.panel1, pos=wx.Point(136, 408),
              size=wx.Size(121, 32), style=0)
        self.btnOcultar.Bind(wx.EVT_BUTTON,
              self.OnBtnOcultar, id=wxID_FRAME1BTNOCULTAR)

        self.btnOcultarLimpar = wx.Button(id=wxID_FRAME1BTNOCULTARLIMPAR,
              label=u'Reset', name=u'btnOcultarLimpar', parent=self.panel1,
              pos=wx.Point(264, 408), size=wx.Size(120, 32), style=0)
        self.btnOcultarLimpar.Bind(wx.EVT_BUTTON,
              self.OnBtnOcultarLimpar, id=wxID_FRAME1BTNOCULTARLIMPAR)

        self.btnOcultarProcurar = wx.Button(id=wxID_FRAME1BTNOCULTARPROCURAR,
              label=u'Choose...', name=u'btnOcultarProcurar',
              parent=self.panel1, pos=wx.Point(424, 88), size=wx.Size(75, 23),
              style=0)
        self.btnOcultarProcurar.Bind(wx.EVT_BUTTON,
              self.OnBtnOcultarProcurar, id=wxID_FRAME1BTNOCULTARPROCURAR)

        self.txtArquivoOcultar = wx.TextCtrl(id=wxID_FRAME1TXTARQUIVOOCULTAR,
              name=u'txtArquivoOcultar', parent=self.panel1, pos=wx.Point(320,
              56), size=wx.Size(176, 21), style=0, value=u'')

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(537, 458),
              style=wx.TAB_TRAVERSAL)

        self.txtRecuperarMsg = wx.TextCtrl(id=wxID_FRAME1TXTRECUPERARMSG,
              name=u'txtRecuperarMsg', parent=self.panel2, pos=wx.Point(8, 16),
              size=wx.Size(280, 368),
              style=wx.TE_READONLY | wx.TE_MULTILINE | wx.VSCROLL, value=u'')

        self.btnRecuperarSair = wx.Button(id=wxID_FRAME1BTNRECUPERARSAIR,
              label=u'Quit', name=u'btnRecuperarSair', parent=self.panel2,
              pos=wx.Point(392, 408), size=wx.Size(121, 32), style=0)
        self.btnRecuperarSair.Bind(wx.EVT_BUTTON,
              self.OnBtnRecuperarSair, id=wxID_FRAME1BTNRECUPERARSAIR)

        self.rdOcultarSim = wx.RadioButton(id=wxID_FRAME1RDOCULTARSIM,
              label=u'Yes', name=u'rdOcultarSim', parent=self.panel1,
              pos=wx.Point(368, 176), size=wx.Size(81, 13), style=0)
        self.rdOcultarSim.SetValue(True)

        self.rbOcultarNao = wx.RadioButton(id=wxID_FRAME1RBOCULTARNAO,
              label=u'No', name=u'rbOcultarNao', parent=self.panel1,
              pos=wx.Point(368, 208), size=wx.Size(81, 13), style=0)
        self.rbOcultarNao.SetValue(True)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Set a key:', name='staticBox1', parent=self.panel1,
              pos=wx.Point(312, 144), size=wx.Size(200, 100), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Choose a file to hide:', name='staticBox2',
              parent=self.panel1, pos=wx.Point(312, 24), size=wx.Size(200, 100),
              style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Key:', name='staticBox3', parent=self.panel1,
              pos=wx.Point(312, 272), size=wx.Size(200, 100), style=0)

        self.txtOcultarChave = wx.TextCtrl(id=wxID_FRAME1TXTOCULTARCHAVE,
              name=u'txtOcultarChave', parent=self.panel1, pos=wx.Point(328,
              312), size=wx.Size(168, 21), style=0, value=u'')

        self.ggOcultar = wx.Gauge(id=wxID_FRAME1GGOCULTAR, name=u'ggOcultar',
              parent=self.panel1, pos=wx.Point(8, 416), range=100,
              size=wx.Size(112, 16), style=wx.GA_HORIZONTAL)

        self.btnRecuperar = wx.Button(id=wxID_FRAME1BTNRECUPERAR,
              label=u'Extract message!', name=u'btnRecuperar', parent=self.panel2,
              pos=wx.Point(136, 408), size=wx.Size(121, 32), style=0)
        self.btnRecuperar.Bind(wx.EVT_BUTTON,
              self.OnBtnRecuperar, id=wxID_FRAME1BTNRECUPERAR)

        self.btnRecuperarLimpar = wx.Button(id=wxID_FRAME1BTNRECUPERARLIMPAR,
              label=u'Reset', name=u'btnRecuperarLimpar', parent=self.panel2,
              pos=wx.Point(264, 408), size=wx.Size(121, 32), style=0)
        self.btnRecuperarLimpar.Bind(wx.EVT_BUTTON,
              self.OnBtnRecuperarLimpar, id=wxID_FRAME1BTNRECUPERARLIMPAR)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Choose a file to extract:', name='staticBox4',
              parent=self.panel2, pos=wx.Point(312, 24), size=wx.Size(200, 100),
              style=0)

        self.txtArquivoRecuperar = wx.TextCtrl(id=wxID_FRAME1TXTARQUIVORECUPERAR,
              name=u'txtArquivoRecuperar', parent=self.panel2, pos=wx.Point(320,
              56), size=wx.Size(176, 21), style=0, value=u'')

        self.btnRecuperarProcurar = wx.Button(id=wxID_FRAME1BTNRECUPERARPROCURAR,
              label=u'Choose...', name=u'btnRecuperarProcurar',
              parent=self.panel2, pos=wx.Point(424, 88), size=wx.Size(75, 23),
              style=0)
        self.btnRecuperarProcurar.Bind(wx.EVT_BUTTON,
              self.OnBtnRecuperarProcurar, id=wxID_FRAME1BTNRECUPERARPROCURAR)

        self.staticBox5 = wx.StaticBox(id=wxID_FRAME1STATICBOX5,
              label=u'Apply a key:', name='staticBox5', parent=self.panel2,
              pos=wx.Point(312, 144), size=wx.Size(200, 100), style=0)

        self.rdRecuperarSim = wx.RadioButton(id=wxID_FRAME1RDRECUPERARSIM,
              label=u'Yes', name=u'rdRecuperarSim', parent=self.panel2,
              pos=wx.Point(368, 176), size=wx.Size(81, 13), style=0)
        self.rdRecuperarSim.SetValue(True)

        self.rdRecuperarNao = wx.RadioButton(id=wxID_FRAME1RDRECUPERARNAO,
              label=u'No', name=u'rdRecuperarNao', parent=self.panel2,
              pos=wx.Point(368, 208), size=wx.Size(81, 13), style=0)
        self.rdRecuperarNao.SetValue(True)

        self.staticBox6 = wx.StaticBox(id=wxID_FRAME1STATICBOX6,
              label=u'Key:', name='staticBox6', parent=self.panel2,
              pos=wx.Point(312, 272), size=wx.Size(200, 100), style=0)

        self.txtRecuperarChave = wx.TextCtrl(id=wxID_FRAME1TXTRECUPERARCHAVE,
              name=u'txtRecuperarChave', parent=self.panel2, pos=wx.Point(328,
              312), size=wx.Size(168, 21), style=0, value=u'')

        self.ggRecuperar = wx.Gauge(id=wxID_FRAME1GGRECUPERAR,
              name=u'ggRecuperar', parent=self.panel2, pos=wx.Point(8, 416),
              range=100, size=wx.Size(112, 16), style=wx.GA_HORIZONTAL)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnOcultarProcurar(self, event):
        self.ProcurarArquivo(self.txtArquivoOcultar, 1)
        event.Skip()

    def OnBtnOcultar(self, event):
        Esteganografia.Ocultar(self.txtOcultarMsg, self.txtArquivoOcultar, self.txtOcultarChave)
        event.Skip()

    def OnBtnOcultarLimpar(self, event):
        self.LimparTexto(self.txtOcultarMsg)
        event.Skip()
    
    def OnBtnOcultarSair(self, event):
        self.Sair()
        event.Skip()

    def OnBtnRecuperarProcurar(self, event):
        self.ProcurarArquivo(self.txtArquivoRecuperar, 0)
        event.Skip()

    def OnBtnRecuperar(self, event):
        sText = Esteganografia.Recuperar(self.txtArquivoRecuperar, self.txtRecuperarChave)
        try:
          self.txtRecuperarMsg.SetValue(str(sText))
        except:
          pass
        event.Skip()

    def OnBtnRecuperarLimpar(self, event):
        self.LimparTexto(self.txtRecuperarMsg)
        event.Skip()
    
    def OnBtnRecuperarSair(self, event):
        self.Sair()
        event.Skip()
        
    def ProcurarArquivo(self, objTxt, iMsg):
        self.dirname = ''
        self.filename = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname,"","*.*", wx.OPEN)
        dlg.SetWildcard("WAV files (*.wav)|*.wav")
        if dlg.ShowModal()==wx.ID_OK:
            self.LimparTexto(objTxt)
            self.filename=dlg.GetFilename()
            Fname = self.filename
            self.dirname=dlg.GetDirectory()
            dlg.Destroy()
            objTxt.write(self.dirname+'\\'+self.filename)
        maxlength = Esteganografia.CharCount(objTxt)
        if iMsg == 1:
          wx.MessageDialog(self, "Allowed message size: "+str(maxlength), 'Message size', 
          wx.OK | wx.ICON_INFORMATION).ShowModal()
        
    def LimparTexto(self, objTxt):
        objTxt.Clear()

    def Sair(self):
        sys.exit(1)
    	
