# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:04:16 2021

@author: gongfei
"""

import shutil
from turtle import width
import xml.dom.minidom
import os
import cv2
from numpy import imag


def xml_zhito_write(boxes,imgpath,w,h):   
    
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         x_min = str(box[1])
         x_max = str(box[2])
         y_min = str(box[3])
         y_max = str(box[4])
         tag = box[0]
    
         nodeobject = doc.createElement('object')
         
         nodename = doc.createElement('name')
         nodename.appendChild(doc.createTextNode(tag))  
         
         nodetruncated = doc.createElement('truncated')
         nodetruncated.appendChild(doc.createTextNode('0'))
         
         
         nodedifficult = doc.createElement('difficult')
         nodedifficult.appendChild(doc.createTextNode('0'))
         nodebndbox = doc.createElement("bndbox")
         nodexmin = doc.createElement("xmin")
         nodexmin.appendChild(doc.createTextNode(x_min))
         nodeymin = doc.createElement("ymin")
         nodeymin.appendChild(doc.createTextNode(y_min))
         nodexmax = doc.createElement("xmax")
         nodexmax.appendChild(doc.createTextNode(x_max))
         nodeymax = doc.createElement("ymax")
         nodeymax.appendChild(doc.createTextNode(y_max))
        
         nodeobject.appendChild(nodename)
         nodeobject.appendChild(nodetruncated)
         nodeobject.appendChild(nodedifficult)
         nodeobject.appendChild(nodebndbox)
         nodebndbox.appendChild(nodexmin)
         nodebndbox.appendChild(nodeymin)
         nodebndbox.appendChild(nodexmax)
         nodebndbox.appendChild(nodeymax)
         
         root.appendChild(nodeobject)
    
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()
    
def xml_zhito_write_v2(boxes,imgpath,w,h):   
    
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         tag = box[0]
         if tag != 'crop':
             x_min = str(box[1])
             x_max = str(box[2])
             y_min = str(box[3])
             y_max = str(box[4])
             relate_id = str(box[-1])
             
             nodeobject = doc.createElement('object')
             
             nodename = doc.createElement('name')
             nodename.appendChild(doc.createTextNode(tag))  
             
             nodetruncated = doc.createElement('truncated')
             nodetruncated.appendChild(doc.createTextNode('0'))
             
             
             nodedifficult = doc.createElement('difficult')
             nodedifficult.appendChild(doc.createTextNode('0'))
             
             noderelated   = doc.createElement('extra')
             noderelated.appendChild(doc.createTextNode(relate_id))
             
             nodebndbox = doc.createElement("bndbox")
             nodexmin = doc.createElement("xmin")
             nodexmin.appendChild(doc.createTextNode(x_min))
             nodeymin = doc.createElement("ymin")
             nodeymin.appendChild(doc.createTextNode(y_min))
             nodexmax = doc.createElement("xmax")
             nodexmax.appendChild(doc.createTextNode(x_max))
             nodeymax = doc.createElement("ymax")
             nodeymax.appendChild(doc.createTextNode(y_max))
        
             nodeobject.appendChild(nodename)
             nodeobject.appendChild(nodetruncated)
             nodeobject.appendChild(nodedifficult)
             nodeobject.appendChild(noderelated)
    
    
             nodeobject.appendChild(nodebndbox)
             nodebndbox.appendChild(nodexmin)
             nodebndbox.appendChild(nodeymin)
             nodebndbox.appendChild(nodexmax)
             nodebndbox.appendChild(nodeymax)
             
             root.appendChild(nodeobject)
             
         elif tag == 'crop':
             crop_xmin = str(box[1])
             crop_xmax = str(box[2])
             crop_ymin = str(box[3])
             crop_ymax = str(box[4])
             
             nodecrop = doc.createElement('crop')
             nodecrop_xmin = doc.createElement('crop_xmin')
             nodecrop_xmin.appendChild(doc.createTextNode(crop_xmin))

             nodecrop_xmax = doc.createElement("crop_xmax")
             nodecrop_xmax.appendChild(doc.createTextNode(crop_xmax))
             
             nodecrop_ymin = doc.createElement("crop_ymin")
             nodecrop_ymin.appendChild(doc.createTextNode(crop_ymin))
             
             nodecrop_ymax = doc.createElement("crop_ymax")
             nodecrop_ymax.appendChild(doc.createTextNode(crop_ymax))  
             
             nodecrop.appendChild(nodecrop_xmin)
             nodecrop.appendChild(nodecrop_xmax)
             nodecrop.appendChild(nodecrop_ymin)
             nodecrop.appendChild(nodecrop_ymax)

             root.appendChild(nodecrop) 
             
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()

def xml_zhito_write_baidu(boxes,imgpath,w,h):   
    #boxes: [class_name,related,xmin,ymin,xmax,ymax]
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         box_name  = box[0]          
         relate_id = str(box[1])
         x_min     = str(box[2])
         x_max     = str(box[4])
         y_min     = str(box[3])
         y_max     = str(box[5])
         
         nodeobject = doc.createElement('object')
         
         nodename = doc.createElement('name')
         nodename.appendChild(doc.createTextNode(box_name))  
         
         nodetruncated = doc.createElement('truncated')
         nodetruncated.appendChild(doc.createTextNode('0'))
         
         
         nodedifficult = doc.createElement('difficult')
         nodedifficult.appendChild(doc.createTextNode('0'))
         
         noderelated   = doc.createElement('extra')
         noderelated.appendChild(doc.createTextNode(relate_id))
         
         nodebndbox = doc.createElement("bndbox")
         nodexmin = doc.createElement("xmin")
         nodexmin.appendChild(doc.createTextNode(x_min))
         nodeymin = doc.createElement("ymin")
         nodeymin.appendChild(doc.createTextNode(y_min))
         nodexmax = doc.createElement("xmax")
         nodexmax.appendChild(doc.createTextNode(x_max))
         nodeymax = doc.createElement("ymax")
         nodeymax.appendChild(doc.createTextNode(y_max))
    
         nodeobject.appendChild(nodename)
         nodeobject.appendChild(nodetruncated)
         nodeobject.appendChild(nodedifficult)
         nodeobject.appendChild(noderelated)


         nodeobject.appendChild(nodebndbox)
         nodebndbox.appendChild(nodexmin)
         nodebndbox.appendChild(nodeymin)
         nodebndbox.appendChild(nodexmax)
         nodebndbox.appendChild(nodeymax)
         
         root.appendChild(nodeobject)
             
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()
    
def xml_zhito_write_lateral(boxes,imgpath,w,h):   
    
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         tag = box[0]
         if tag != 'crop':
             x_min = str(box[1])
             x_max = str(box[2])
             y_min = str(box[3])
             y_max = str(box[4])
             relate_id = str(box[-1])
             
             nodeobject = doc.createElement('object')
             
             nodename = doc.createElement('name')
             nodename.appendChild(doc.createTextNode(tag))  
             
             nodetruncated = doc.createElement('truncated')
             nodetruncated.appendChild(doc.createTextNode('0'))
             
             
             nodedifficult = doc.createElement('difficult')
             nodedifficult.appendChild(doc.createTextNode('0'))
             
             noderelated   = doc.createElement('extra')
             noderelated.appendChild(doc.createTextNode(relate_id))
             
             nodebndbox = doc.createElement("bndbox")
             nodexmin = doc.createElement("xmin")
             nodexmin.appendChild(doc.createTextNode(x_min))
             nodeymin = doc.createElement("ymin")
             nodeymin.appendChild(doc.createTextNode(y_min))
             nodexmax = doc.createElement("xmax")
             nodexmax.appendChild(doc.createTextNode(x_max))
             nodeymax = doc.createElement("ymax")
             nodeymax.appendChild(doc.createTextNode(y_max))
        
             nodeobject.appendChild(nodename)
             nodeobject.appendChild(nodetruncated)
             nodeobject.appendChild(nodedifficult)
             nodeobject.appendChild(noderelated)
    
    
             nodeobject.appendChild(nodebndbox)
             nodebndbox.appendChild(nodexmin)
             nodebndbox.appendChild(nodeymin)
             nodebndbox.appendChild(nodexmax)
             nodebndbox.appendChild(nodeymax)
             
             root.appendChild(nodeobject)
             
         elif tag == 'crop':
             crop_xmin = str(box[1])
             crop_xmax = str(box[2])
             crop_ymin = str(box[3])
             crop_ymax = str(box[4])
             
             nodecrop = doc.createElement('crop')
             nodecrop_xmin = doc.createElement('crop_xmin')
             nodecrop_xmin.appendChild(doc.createTextNode(crop_xmin))

             nodecrop_xmax = doc.createElement("crop_xmax")
             nodecrop_xmax.appendChild(doc.createTextNode(crop_xmax))
             
             nodecrop_ymin = doc.createElement("crop_ymin")
             nodecrop_ymin.appendChild(doc.createTextNode(crop_ymin))
             
             nodecrop_ymax = doc.createElement("crop_ymax")
             nodecrop_ymax.appendChild(doc.createTextNode(crop_ymax))  
             
             nodecrop.appendChild(nodecrop_xmin)
             nodecrop.appendChild(nodecrop_xmax)
             nodecrop.appendChild(nodecrop_ymin)
             nodecrop.appendChild(nodecrop_ymax)

             root.appendChild(nodecrop) 
             
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()
    

def xml_zhito_merge(boxes,imgpath,w,h):   
    
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         x_min = str(box[1])
         y_min = str(box[2])
         x_max = str(box[3])
         y_max = str(box[4])
         tag = box[0]
    
         nodeobject = doc.createElement('object')
         
         nodename = doc.createElement('name')
         nodename.appendChild(doc.createTextNode(tag))  
         
         nodetruncated = doc.createElement('truncated')
         nodetruncated.appendChild(doc.createTextNode('0'))
         
         
         nodedifficult = doc.createElement('difficult')
         nodedifficult.appendChild(doc.createTextNode('0'))
         nodebndbox = doc.createElement("bndbox")
         nodexmin = doc.createElement("xmin")
         nodexmin.appendChild(doc.createTextNode(x_min))
         nodeymin = doc.createElement("ymin")
         nodeymin.appendChild(doc.createTextNode(y_min))
         nodexmax = doc.createElement("xmax")
         nodexmax.appendChild(doc.createTextNode(x_max))
         nodeymax = doc.createElement("ymax")
         nodeymax.appendChild(doc.createTextNode(y_max))
        
         nodeobject.appendChild(nodename)
         nodeobject.appendChild(nodetruncated)
         nodeobject.appendChild(nodedifficult)
         nodeobject.appendChild(nodebndbox)
         nodebndbox.appendChild(nodexmin)
         nodebndbox.appendChild(nodeymin)
         nodebndbox.appendChild(nodexmax)
         nodebndbox.appendChild(nodeymax)
         
         root.appendChild(nodeobject)
    
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()


def xml_zhito_merge_v2(boxes,imgpath,w,h):   
    
    fd,jpg_fn = os.path.split(imgpath)
    fdn, ext  = os.path.splitext(imgpath)
    xml_fn    = fdn  + '.xml'
    
    
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    
    for box in boxes:
         x_min = str(box[1])
         y_min = str(box[2])
         x_max = str(box[3])
         y_max = str(box[4])
         tag = box[0]
         relate_id = str(box[-1])
    
         nodeobject = doc.createElement('object')
         
         nodename = doc.createElement('name')
         nodename.appendChild(doc.createTextNode(tag))  
         
         nodetruncated = doc.createElement('truncated')
         nodetruncated.appendChild(doc.createTextNode('0'))
         nodedifficult = doc.createElement('difficult')
         nodedifficult.appendChild(doc.createTextNode('0'))
         noderelated   = doc.createElement('extra')
         noderelated.appendChild(doc.createTextNode(relate_id))
         
         nodebndbox = doc.createElement("bndbox")
         nodexmin = doc.createElement("xmin")
         nodexmin.appendChild(doc.createTextNode(x_min))
         nodeymin = doc.createElement("ymin")
         nodeymin.appendChild(doc.createTextNode(y_min))
         nodexmax = doc.createElement("xmax")
         nodexmax.appendChild(doc.createTextNode(x_max))
         nodeymax = doc.createElement("ymax")
         nodeymax.appendChild(doc.createTextNode(y_max))
         
        
         nodeobject.appendChild(nodename)
         nodeobject.appendChild(nodetruncated)
         nodeobject.appendChild(nodedifficult)
         nodeobject.appendChild(noderelated)

         nodeobject.appendChild(nodebndbox)
         nodebndbox.appendChild(nodexmin)
         nodebndbox.appendChild(nodeymin)
         nodebndbox.appendChild(nodexmax)
         nodebndbox.appendChild(nodeymax)
         
         root.appendChild(nodeobject)
    
    fp = open(xml_fn, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()



def xml_zhito_write_baidu_xl(ignore_points_all,box3d_all,image_name,image,img_h,img_w):   
    #boxes: [class_name,related,xmin,ymin,xmax,ymax]
    # fd,jpg_fn = os.path.split(imgpath)
    # fdn, ext  = os.path.splitext(imgpath)
    # xml_fn    = fdn  + '.xml'
    xml_name=image_name.replace('.jpg','.xml')
    ##creat save folder###
    fd='./save/'
    jpg_fn=image_name
    image_save_path=fd+image_name
    xml_save_path  =fd+xml_name
    imgpath=image_save_path

   
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root) 
    
    nodefoldername = doc.createElement('folder')
    nodefoldername.appendChild(doc.createTextNode(fd))
    
    nodefilename = doc.createElement('filename')
    nodefilename.appendChild(doc.createTextNode(jpg_fn))
    
    nodepath = doc.createElement('path')
    nodepath.appendChild(doc.createTextNode(imgpath))
    
    nodesource = doc.createElement('source')
    nodesource.appendChild(doc.createTextNode('Unknown'))
    
    nodesize = doc.createElement('size')
    nodewidth = doc.createElement("width")
    nodewidth.appendChild(doc.createTextNode(str(img_w)))
    nodeheight = doc.createElement("height")
    nodeheight.appendChild(doc.createTextNode(str(img_h)))
    nodedepth = doc.createElement("depth")
    nodedepth.appendChild(doc.createTextNode('3'))  
    
    nodesegmented = doc.createElement('segmented')
    nodesegmented.appendChild(doc.createTextNode('0'))
     
    nodesize.appendChild(nodewidth)
    nodesize.appendChild(nodeheight)
    nodesize.appendChild(nodedepth)
    
    root.appendChild(nodefoldername)
    root.appendChild(nodefilename)
    root.appendChild(nodepath)
    root.appendChild(nodesource)
    root.appendChild(nodesegmented)
    root.appendChild(nodesize) 
    for ele in box3d_all:
        obj_id  = ele["Obj_id"]
        Points8 = ele["Points"]
        box2d   = ele["box2d"]
        orientation  = ele["orientation"]
        vehicle_name = ele["transportation"]
        if vehicle_name=='minibus':
            vehicle_name='car'
        if vehicle_name=='construction_truck':
            vehicle_name='truck'
        occlusion    = int(ele["occlusion"])
        truncation   = int(ele["truncation"])
        orientation_occlusion=int(ele["orientation_occlusion"])
        orientation_truncation=int(ele["orientation_truncation"])
############init variable########################################        
        vehicle_xmin = None
        vehicle_ymin = None
        vehicle_xmax = None
        vehicle_ymax = None

        headtail_xmin = None
        headtail_ymin = None
        headtail_xmax = None
        headtail_ymax = None
        d1=None
        d2=None
#####################vehicle_body_node#########################
        # if (len(box2d) > 0 and truncation != 2 and occlusion != 2):
        
        if len(box2d)>0 :

            vehicle_xmin0 = box2d["Points"][0]["x"]
            vehicle_ymin0 = box2d["Points"][0]["y"]
            vehicle_xmax0 = box2d["Points"][1]["x"]
            vehicle_ymax0 = box2d["Points"][1]["y"]

            vehicle_xmin = max(1,round(vehicle_xmin0))
            vehicle_ymin = max(1,round(vehicle_ymin0))
            vehicle_xmax = min(img_w,round(vehicle_xmax0))
            vehicle_ymax = min(img_h,round(vehicle_ymax0))
            vehicle_width0=vehicle_xmax0-vehicle_xmin0

            # if truncation != 2 and occlusion != 2 and vehicle_width>12 :
            if vehicle_width0>12 and truncation != 2:
                nodeobject = doc.createElement('object')
                
                nodename = doc.createElement('name')
                nodename.appendChild(doc.createTextNode(vehicle_name))  
                
                nodetruncation = doc.createElement('truncation')
                nodetruncation.appendChild(doc.createTextNode(str(truncation)))

                nodeoriention = doc.createElement('oriention')
                nodeoriention.appendChild(doc.createTextNode(str(orientation)))

                nodeocclusion = doc.createElement('occlusion')
                nodeocclusion.appendChild(doc.createTextNode(str(occlusion)))
                        
                # nodedifficult = doc.createElement('difficult')
                # nodedifficult.appendChild(doc.createTextNode('0'))
                
                noderelated   = doc.createElement('extra')
                noderelated.appendChild(doc.createTextNode(obj_id))
                
                nodebndbox = doc.createElement("bndbox")
                nodexmin = doc.createElement("xmin")
                nodexmin.appendChild(doc.createTextNode(str(vehicle_xmin)))
                nodeymin = doc.createElement("ymin")
                nodeymin.appendChild(doc.createTextNode(str(vehicle_ymin)))
                nodexmax = doc.createElement("xmax")
                nodexmax.appendChild(doc.createTextNode(str(vehicle_xmax)))
                nodeymax = doc.createElement("ymax")
                nodeymax.appendChild(doc.createTextNode(str(vehicle_ymax)))
            
                nodeobject.appendChild(nodename)
                nodeobject.appendChild(nodetruncation)
                nodeobject.appendChild(nodeoriention)
                nodeobject.appendChild(nodeocclusion)

                nodeobject.appendChild(noderelated)


                nodeobject.appendChild(nodebndbox)
                nodebndbox.appendChild(nodexmin)
                nodebndbox.appendChild(nodeymin)
                nodebndbox.appendChild(nodexmax)
                nodebndbox.appendChild(nodeymax)
                
                root.appendChild(nodeobject)
##################serious truction or occlusion is labeled ignore#####################
            # if (truncation == 2 or occlusion == 2) :
            #     uuid      = "-1"
            #     ig_xmin = max(1,round(vehicle_xmin))
            #     ig_ymin = max(1,round(vehicle_ymin))
            #     ig_xmax = min(img_w,round(vehicle_xmax))
            #     ig_ymax = min(img_h,round(vehicle_ymax))

                
            #     nodeobject = doc.createElement('object')
                
            #     nodename = doc.createElement('name')
            #     nodename.appendChild(doc.createTextNode('ignore'))  
                
            #     nodetruncated = doc.createElement('truncated')
            #     nodetruncated.appendChild(doc.createTextNode(uuid))
                
                
            #     nodedifficult = doc.createElement('difficult')
            #     nodedifficult.appendChild(doc.createTextNode(uuid))
                
            #     noderelated   = doc.createElement('extra')
            #     noderelated.appendChild(doc.createTextNode(uuid))
                
            #     nodebndbox = doc.createElement("bndbox")
            #     nodexmin = doc.createElement("xmin")
            #     nodexmin.appendChild(doc.createTextNode(str(ig_xmin)))
            #     nodeymin = doc.createElement("ymin")
            #     nodeymin.appendChild(doc.createTextNode(str(ig_ymin)))
            #     nodexmax = doc.createElement("xmax")
            #     nodexmax.appendChild(doc.createTextNode(str(ig_xmax)))
            #     nodeymax = doc.createElement("ymax")
            #     nodeymax.appendChild(doc.createTextNode(str(ig_ymax)))
            
            #     nodeobject.appendChild(nodename)
            #     nodeobject.appendChild(nodetruncated)
            #     nodeobject.appendChild(nodedifficult)
            #     nodeobject.appendChild(noderelated)


            #     nodeobject.appendChild(nodebndbox)
            #     nodebndbox.appendChild(nodexmin)
            #     nodebndbox.appendChild(nodeymin)
            #     nodebndbox.appendChild(nodexmax)
            #     nodebndbox.appendChild(nodeymax)
                
            #     root.appendChild(nodeobject)


            
############################headtail_node############################################
        if len(Points8)>0 and len(box2d)>0:       
            headtail_name = vehicle_name + "_" + orientation
            headtail_xmin0 = Points8[0]["x"]
            headtail_ymin0 = Points8[0]["y"]
            headtail_xmax0 = Points8[2]["x"]
            headtail_ymax0 = Points8[2]["y"]

            headtail_xmin = max(1,round(headtail_xmin0))
            headtail_ymin = max(1,round(headtail_ymin0))
            headtail_xmax = min(img_w,round(headtail_xmax0))
            headtail_ymax = min(img_h,round(headtail_ymax0))
            headtail_width0 = headtail_xmax0 - headtail_xmin0
            ratio= headtail_width0/vehicle_width0
            if (orientation == "head" or orientation == "tail") and (orientation_truncation !=2 and orientation_occlusion != 2) and (headtail_width0>12) and (ratio>1/3):


                nodeobject = doc.createElement('object')
                
                nodename = doc.createElement('name')
                nodename.appendChild(doc.createTextNode(headtail_name))  
                
                nodetruncation = doc.createElement('orientation_truncation')
                nodetruncation.appendChild(doc.createTextNode(str(orientation_truncation)))

                # nodeoriention = doc.createElement('oriention')
                # nodeoriention.appendChild(doc.createTextNode(str(orientation)))

                nodeocclusion = doc.createElement('orientation_occlusion')
                nodeocclusion.appendChild(doc.createTextNode(str(orientation_occlusion)))
                        
                # nodedifficult = doc.createElement('difficult')
                # nodedifficult.appendChild(doc.createTextNode('0'))
                
                noderelated   = doc.createElement('extra')
                noderelated.appendChild(doc.createTextNode(obj_id))
                
                nodebndbox = doc.createElement("bndbox")
                nodexmin = doc.createElement("xmin")
                nodexmin.appendChild(doc.createTextNode(str(headtail_xmin)))
                nodeymin = doc.createElement("ymin")
                nodeymin.appendChild(doc.createTextNode(str(headtail_ymin)))
                nodexmax = doc.createElement("xmax")
                nodexmax.appendChild(doc.createTextNode(str(headtail_xmax)))
                nodeymax = doc.createElement("ymax")
                nodeymax.appendChild(doc.createTextNode(str(headtail_ymax)))
            
                nodeobject.appendChild(nodename)
                nodeobject.appendChild(nodetruncation)
                # nodeobject.appendChild(nodeoriention)
                nodeobject.appendChild(nodeocclusion)

                nodeobject.appendChild(noderelated)


                nodeobject.appendChild(nodebndbox)
                nodebndbox.appendChild(nodexmin)
                nodebndbox.appendChild(nodeymin)
                nodebndbox.appendChild(nodexmax)
                nodebndbox.appendChild(nodeymax)
                
                root.appendChild(nodeobject)
########################vehicle_half_node############################################
            if (vehicle_xmin is not None) and (headtail_xmin is not None):
                d1 = abs(vehicle_xmin - headtail_xmin)
            if (vehicle_xmax is not None) and (headtail_xmax is not None):
                d2 = abs(vehicle_xmax - headtail_xmax)
        # if (vehicle_xmin is not None) and (vehicle_xmax is not None):
        #     d3 = vehicle_xmax - vehicle_xmin
        # if (headtail_xmin is not None) and (headtail_xmax is not None):
        #     d4 = headtail_xmax - headtail_xmin
        # if ((orientation == "head" or orientation == "tail") and ((d1 is not None)or (d2 is not None)) and (d1 >=16 or d2 >= 16)):
         
            # if ((orientation == "head" or orientation == "tail") and ((d1 is not None) or (d2 is not None)) and (d1 >=16 or d2 >= 16)) and ((d3 is not None) and (d4 is not None)) and (d4/d3 >= 1/6):
            # if ((orientation == "head" or orientation == "tail") and ((d1 is not None) or (d2 is not None)) and (d1 >=16 or d2 >= 16))  and (ratio >= 1/4):
            if (orientation == "head" or orientation == "tail")  and (d1 >=16 or d2 >= 16)  and (ratio >= 1/3 and ratio <= 0.85) and  (truncation != 2 and occlusion != 2):


                half_name = vehicle_name + "_" + "half"
                half_xmin = min( Points8[0]["x"], Points8[1]["x"], Points8[2]["x"], Points8[3]["x"], Points8[4]["x"], Points8[5]["x"], Points8[6]["x"], Points8[7]["x"])
                half_ymin = min( Points8[0]["y"], Points8[1]["y"], Points8[2]["y"], Points8[3]["y"], Points8[4]["y"], Points8[5]["y"], Points8[6]["y"], Points8[7]["y"])
                half_xmax = max( Points8[0]["x"], Points8[1]["x"], Points8[2]["x"], Points8[3]["x"], Points8[4]["x"], Points8[5]["x"], Points8[6]["x"], Points8[7]["x"])
                half_ymax = Points8[7]["y"]

                half_xmin = max(1,round(half_xmin))
                half_ymin = max(1,round(half_ymin))
                half_xmax = min(img_w,round(half_xmax))
                half_ymax = min(img_h,round(half_ymax))



                nodeobject = doc.createElement('object')
                nodename = doc.createElement('name')
                nodename.appendChild(doc.createTextNode(half_name))  
                
                # nodetruncation = doc.createElement('orientation_truncation')
                # nodetruncation.appendChild(doc.createTextNode(str(orientation_truncation)))

                # nodeoriention = doc.createElement('oriention')
                # nodeoriention.appendChild(doc.createTextNode(str(orientation)))

                # nodeocclusion = doc.createElement('orientation_occlusion')
                # nodeocclusion.appendChild(doc.createTextNode(str(orientation_occlusion)))
                        
                # nodedifficult = doc.createElement('difficult')
                # nodedifficult.appendChild(doc.createTextNode('0'))
                
                noderelated   = doc.createElement('extra')
                noderelated.appendChild(doc.createTextNode(obj_id))
                
                nodebndbox = doc.createElement("bndbox")
                nodexmin = doc.createElement("xmin")
                nodexmin.appendChild(doc.createTextNode(str(half_xmin)))
                nodeymin = doc.createElement("ymin")
                nodeymin.appendChild(doc.createTextNode(str(half_ymin)))
                nodexmax = doc.createElement("xmax")
                nodexmax.appendChild(doc.createTextNode(str(half_xmax)))
                nodeymax = doc.createElement("ymax")
                nodeymax.appendChild(doc.createTextNode(str(half_ymax)))
            
                nodeobject.appendChild(nodename)
                # nodeobject.appendChild(nodetruncation)
                # nodeobject.appendChild(nodeoriention)
                # nodeobject.appendChild(nodeocclusion)

                nodeobject.appendChild(noderelated)


                nodeobject.appendChild(nodebndbox)
                nodebndbox.appendChild(nodexmin)
                nodebndbox.appendChild(nodeymin)
                nodebndbox.appendChild(nodexmax)
                nodebndbox.appendChild(nodeymax)
                
                root.appendChild(nodeobject)






################ignore_node#############################################
    for ig in ignore_points_all:
        uuid      = "-1"
        ig_points = ig["Points"]
        ig_xmin = ig_points[0]["x"]
        ig_ymin = ig_points[0]["y"]
        ig_xmax = ig_points[1]["x"]
        ig_ymax = ig_points[1]["y"]

        ig_xmin = max(1,round(ig_xmin))
        ig_ymin = max(1,round(ig_ymin))
        ig_xmax = min(img_w,round(ig_xmax))
        ig_ymax = min(img_h,round(ig_ymax))

         
        nodeobject = doc.createElement('object')
         
        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode('ignore'))  
         
        nodetruncated = doc.createElement('truncated')
        nodetruncated.appendChild(doc.createTextNode(uuid))
         
         
        nodedifficult = doc.createElement('difficult')
        nodedifficult.appendChild(doc.createTextNode(uuid))
         
        noderelated   = doc.createElement('extra')
        noderelated.appendChild(doc.createTextNode(uuid))
         
        nodebndbox = doc.createElement("bndbox")
        nodexmin = doc.createElement("xmin")
        nodexmin.appendChild(doc.createTextNode(str(ig_xmin)))
        nodeymin = doc.createElement("ymin")
        nodeymin.appendChild(doc.createTextNode(str(ig_ymin)))
        nodexmax = doc.createElement("xmax")
        nodexmax.appendChild(doc.createTextNode(str(ig_xmax)))
        nodeymax = doc.createElement("ymax")
        nodeymax.appendChild(doc.createTextNode(str(ig_ymax)))
    
        nodeobject.appendChild(nodename)
        nodeobject.appendChild(nodetruncated)
        nodeobject.appendChild(nodedifficult)
        nodeobject.appendChild(noderelated)


        nodeobject.appendChild(nodebndbox)
        nodebndbox.appendChild(nodexmin)
        nodebndbox.appendChild(nodeymin)
        nodebndbox.appendChild(nodexmax)
        nodebndbox.appendChild(nodeymax)
         
        root.appendChild(nodeobject)
             
    fp = open(xml_save_path, 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    fp.close()
    cv2.imwrite(image_save_path,image)
