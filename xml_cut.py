



from configparser import Interpolation
from tkinter import Scale
import cv2
import os
import xml.etree.ElementTree as ET
import shutil
import matplotlib.pyplot as plt
import xml.dom.minidom
import random
def get_bbox_xyxy(obj):
    vehicle_class=obj.find("name").text.strip()
    bbox=obj.find("bndbox")
    xmin=int(bbox.find("xmin").text)
    ymin=int(bbox.find("ymin").text)
    xmax=int(bbox.find("xmax").text)
    ymax=int(bbox.find("ymax").text)
    id=int(obj.find("extra").text)
    print(id)
    return [vehicle_class,xmin,ymin,xmax,ymax,id]


def read_write_xml(image_path):
    fd,image_name=os.path.split(image_path)
    image_name_origin=image_name.replace(".jpg",'')
    xml_name=image_name.replace(".jpg",".xml")
    # xml_name="./save_cut/"+xml_name
    image=cv2.imread(image_path)
    size=image.shape
    image_w=size[1]
    image_h=size[0]
    #####read_origin_xml#########
    xml_path=image_path.replace(".jpg",".xml")
    tree=ET.parse(xml_path)
    root_read=tree.getroot()
    ######write_new_xml#########
   
    car=None
    car_head=None
    car_tail=None
    car_half=None
     
    for obj in root_read.iter('object'):
       
        bbox=get_bbox_xyxy(obj)
        vehicle_part=bbox[0]
        xmin=bbox[1]
        ymin=bbox[2]
        xmax=bbox[3]
        ymax=bbox[4]
        id  =bbox[5]
        if vehicle_part=="car":
            print('car')
            car=True
            car_xmin_ori=xmin
            car_ymin_ori=ymin
            car_xmax_ori=xmax
            car_ymax_ori=ymax
        if vehicle_part=="car_head":
            print('car_head')
            car_head=True
            car_head_xmin_ori=xmin
            car_head_ymin_ori=ymin
            car_head_xmax_ori=xmax
            car_head_ymax_ori=ymax
        if vehicle_part=="car_tail":
            print('car_tail')
            car_tail=True
            car_tail_xmin_ori=xmin
            car_tail_ymin_ori=ymin
            car_tail_xmax_ori=xmax
            car_tail_ymax_ori=ymax
        if vehicle_part=="car_half":
            print('car_half')
            car_half=True
            car_half_xmin_ori=xmin
            car_half_ymin_ori=ymin
            car_half_xmax_ori=xmax
            car_half_ymax_ori=ymax
    # if car and (car_head is None) and (car_tail is None) and (car_half is None):  
    #     print("lateral car")
    #     image_name_origin=image_name.replace(".jpg",'')
    #     for i in range(car_xmin_ori,int((car_xmin_ori+car_xmax_ori)/2)):   
    #         car_xmin=i
    #         car_xmax=car_xmax_ori
    #         car_ymin=car_ymin_ori
    #         car_ymax=car_ymax_ori

    #         image_cut=image[1:image_h,i:image_w] 
    #         image_name=image_name_origin+f'_{i}.jpg'
    #         image_path=os.path.join("./save_cut/",image_name)
    #         cv2.imwrite(image_path,image_cut)
            
    #         doc = xml.dom.minidom.Document()
    #         root = doc.createElement('annotation')
    #         doc.appendChild(root) 
        
    #         nodefoldername = doc.createElement('folder')
    #         nodefoldername.appendChild(doc.createTextNode(fd))
                
    #         nodefilename = doc.createElement('filename')
    #         nodefilename.appendChild(doc.createTextNode(image_name))
                
    #         nodepath = doc.createElement('path')
    #         nodepath.appendChild(doc.createTextNode(image_path))
                
    #         nodesource = doc.createElement('source')
    #         nodesource.appendChild(doc.createTextNode('Unknown'))
                
    #         nodesize = doc.createElement('size')
    #         nodewidth = doc.createElement("width")
    #         nodewidth.appendChild(doc.createTextNode(str(image_w)))
    #         nodeheight = doc.createElement("height")
    #         nodeheight.appendChild(doc.createTextNode(str(image_h)))
    #         nodedepth = doc.createElement("depth")
    #         nodedepth.appendChild(doc.createTextNode('3'))  
                
    #         nodesegmented = doc.createElement('segmented')
    #         nodesegmented.appendChild(doc.createTextNode('0'))
                
    #         nodesize.appendChild(nodewidth)
    #         nodesize.appendChild(nodeheight)
    #         nodesize.appendChild(nodedepth)
                
    #         root.appendChild(nodefoldername)
    #         root.appendChild(nodefilename)
    #         root.appendChild(nodepath)
    #         root.appendChild(nodesource)
    #         root.appendChild(nodesegmented)
    #         root.appendChild(nodesize)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_xmin-i)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_xmax-i)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
            
    #         root.appendChild(nodeobject)
    #         fp = open(os.path.join("./save_cut/"+xml_name.replace(".xml",f"_{i}.xml")), 'w')
    #         doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #         #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    #         fp.close()
    #     for i in range(1,int((car_xmax_ori-car_xmin_ori)/2)): 
    #         car_xmin=car_xmin_ori
    #         car_xmax=car_xmax_ori-i
    #         car_ymin=car_ymin_ori
    #         car_ymax=car_ymax_ori

    #         image_cut=image[1:image_h,1:car_xmax] 
    #         image_name=image_name_origin+f'_-{i}.jpg'
    #         image_path=os.path.join("./save_cut2/",image_name)
    #         cv2.imwrite(image_path,image_cut)
    #         doc = xml.dom.minidom.Document()
    #         root = doc.createElement('annotation')
    #         doc.appendChild(root) 
        
    #         nodefoldername = doc.createElement('folder')
    #         nodefoldername.appendChild(doc.createTextNode(fd))
                
    #         nodefilename = doc.createElement('filename')
    #         nodefilename.appendChild(doc.createTextNode(image_name))
                
    #         nodepath = doc.createElement('path')
    #         nodepath.appendChild(doc.createTextNode(image_path))
                
    #         nodesource = doc.createElement('source')
    #         nodesource.appendChild(doc.createTextNode('Unknown'))
                
    #         nodesize = doc.createElement('size')
    #         nodewidth = doc.createElement("width")
    #         nodewidth.appendChild(doc.createTextNode(str(image_w)))
    #         nodeheight = doc.createElement("height")
    #         nodeheight.appendChild(doc.createTextNode(str(image_h)))
    #         nodedepth = doc.createElement("depth")
    #         nodedepth.appendChild(doc.createTextNode('3'))  
                
    #         nodesegmented = doc.createElement('segmented')
    #         nodesegmented.appendChild(doc.createTextNode('0'))
                
    #         nodesize.appendChild(nodewidth)
    #         nodesize.appendChild(nodeheight)
    #         nodesize.appendChild(nodedepth)
                
    #         root.appendChild(nodefoldername)
    #         root.appendChild(nodefilename)
    #         root.appendChild(nodepath)
    #         root.appendChild(nodesource)
    #         root.appendChild(nodesegmented)
    #         root.appendChild(nodesize)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_xmin)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_xmax-1)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
    #         root.appendChild(nodeobject)
    #         fp = open(os.path.join("./save_cut2/"+xml_name.replace(".xml",f"_-{i}.xml")), 'w')
    #         doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #         #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    #         fp.close()
    # if car and car_head and car_half and car_xmax_ori-car_head_xmax_ori>100:
    #     print("left out")
    #     for i in range(car_xmin_ori,car_xmin_ori+int((car_xmax_ori-car_xmin_ori)*0.9)):

    #         image_cut=image[1:image_h,i:image_w] 
    #         image_name=image_name_origin+f'_{i}.jpg'
    #         image_path=os.path.join("./save_cut3/",image_name)
    #         cv2.imwrite(image_path,image_cut)

    #         car_xmin=i
    #         car_xmax=car_xmax_ori
    #         car_ymin=car_ymin_ori
    #         car_ymax=car_ymax_ori

    #         car_half_xmin=i
    #         car_half_xmax=car_half_xmax_ori
    #         car_half_ymin=car_half_ymin_ori
    #         car_half_ymax=car_half_ymax_ori
            
            
    #         car_head_xmin=i
    #         car_head_xmax=car_head_xmax_ori
    #         car_head_ymin=car_head_ymin_ori
    #         car_head_ymax=car_head_ymax_ori

    #         doc = xml.dom.minidom.Document()
    #         root = doc.createElement('annotation')
    #         doc.appendChild(root) 
        
    #         nodefoldername = doc.createElement('folder')
    #         nodefoldername.appendChild(doc.createTextNode(fd))
                
    #         nodefilename = doc.createElement('filename')
    #         nodefilename.appendChild(doc.createTextNode(image_name))
                
    #         nodepath = doc.createElement('path')
    #         nodepath.appendChild(doc.createTextNode(image_path))
                
    #         nodesource = doc.createElement('source')
    #         nodesource.appendChild(doc.createTextNode('Unknown'))
                
    #         nodesize = doc.createElement('size')
    #         nodewidth = doc.createElement("width")
    #         nodewidth.appendChild(doc.createTextNode(str(image_w)))
    #         nodeheight = doc.createElement("height")
    #         nodeheight.appendChild(doc.createTextNode(str(image_h)))
    #         nodedepth = doc.createElement("depth")
    #         nodedepth.appendChild(doc.createTextNode('3'))  
                
    #         nodesegmented = doc.createElement('segmented')
    #         nodesegmented.appendChild(doc.createTextNode('0'))
                
    #         nodesize.appendChild(nodewidth)
    #         nodesize.appendChild(nodeheight)
    #         nodesize.appendChild(nodedepth)
                
    #         root.appendChild(nodefoldername)
    #         root.appendChild(nodefilename)
    #         root.appendChild(nodepath)
    #         root.appendChild(nodesource)
    #         root.appendChild(nodesegmented)
    #         root.appendChild(nodesize)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_xmin-i)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_xmax-i)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
            
    #         root.appendChild(nodeobject)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car_half"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_half_xmin-i)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_half_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_half_xmax-i)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_half_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
            
    #         root.appendChild(nodeobject)

    #         if i<int((car_head_xmax_ori-car_head_xmin_ori)/2):

    #             nodeobject = doc.createElement('object')
    #             nodename = doc.createElement('name')
    #             nodename.appendChild(doc.createTextNode("car_head"))  
                
    #             nodetruncated = doc.createElement('truncated')
    #             nodetruncated.appendChild(doc.createTextNode('0'))
    #             nodedifficult = doc.createElement('difficult')
    #             nodedifficult.appendChild(doc.createTextNode('0'))
    #             noderelated   = doc.createElement('extra')
    #             noderelated.appendChild(doc.createTextNode(str(id)))
                
    #             nodebndbox = doc.createElement("bndbox")
    #             nodexmin = doc.createElement("xmin")
    #             nodexmin.appendChild(doc.createTextNode(str(car_head_xmin-i)))
    #             nodeymin = doc.createElement("ymin")
    #             nodeymin.appendChild(doc.createTextNode(str(car_head_ymin)))
    #             nodexmax = doc.createElement("xmax")
    #             nodexmax.appendChild(doc.createTextNode(str(car_head_xmax-i)))
    #             nodeymax = doc.createElement("ymax")
    #             nodeymax.appendChild(doc.createTextNode(str(car_head_ymax)))
                
                
    #             nodeobject.appendChild(nodename)
    #             nodeobject.appendChild(nodetruncated)
    #             nodeobject.appendChild(nodedifficult)
    #             nodeobject.appendChild(noderelated)

    #             nodeobject.appendChild(nodebndbox)
    #             nodebndbox.appendChild(nodexmin)
    #             nodebndbox.appendChild(nodeymin)
    #             nodebndbox.appendChild(nodexmax)
    #             nodebndbox.appendChild(nodeymax)
                
    #             root.appendChild(nodeobject)
    #         fp = open(os.path.join("./save_cut3/"+xml_name.replace(".xml",f"_{i}.xml")), 'w')
    #         doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #         #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    #         fp.close()

    
    # if car and car_tail and car_half and car_xmax_ori-car_tail_xmax_ori>100:
    #     print("left in")
    #     for i in range(car_xmin_ori,car_xmin_ori+int((car_xmax_ori-car_xmin_ori)*0.9)):

    #         image_cut=image[1:image_h,i:image_w] 
    #         image_name=image_name_origin+f'_{i}.jpg'
    #         image_path=os.path.join("./save_cut4/",image_name)
    #         cv2.imwrite(image_path,image_cut)

    #         car_xmin=i
    #         car_xmax=car_xmax_ori
    #         car_ymin=car_ymin_ori
    #         car_ymax=car_ymax_ori

    #         car_half_xmin=i
    #         car_half_xmax=car_half_xmax_ori
    #         car_half_ymin=car_half_ymin_ori
    #         car_half_ymax=car_half_ymax_ori
            
            
    #         car_tail_xmin=i
    #         car_tail_xmax=car_tail_xmax_ori
    #         car_tail_ymin=car_tail_ymin_ori
    #         car_tail_ymax=car_tail_ymax_ori

    #         doc = xml.dom.minidom.Document()
    #         root = doc.createElement('annotation')
    #         doc.appendChild(root) 
        
    #         nodefoldername = doc.createElement('folder')
    #         nodefoldername.appendChild(doc.createTextNode(fd))
                
    #         nodefilename = doc.createElement('filename')
    #         nodefilename.appendChild(doc.createTextNode(image_name))
                
    #         nodepath = doc.createElement('path')
    #         nodepath.appendChild(doc.createTextNode(image_path))
                
    #         nodesource = doc.createElement('source')
    #         nodesource.appendChild(doc.createTextNode('Unknown'))
                
    #         nodesize = doc.createElement('size')
    #         nodewidth = doc.createElement("width")
    #         nodewidth.appendChild(doc.createTextNode(str(image_w)))
    #         nodeheight = doc.createElement("height")
    #         nodeheight.appendChild(doc.createTextNode(str(image_h)))
    #         nodedepth = doc.createElement("depth")
    #         nodedepth.appendChild(doc.createTextNode('3'))  
                
    #         nodesegmented = doc.createElement('segmented')
    #         nodesegmented.appendChild(doc.createTextNode('0'))
                
    #         nodesize.appendChild(nodewidth)
    #         nodesize.appendChild(nodeheight)
    #         nodesize.appendChild(nodedepth)
                
    #         root.appendChild(nodefoldername)
    #         root.appendChild(nodefilename)
    #         root.appendChild(nodepath)
    #         root.appendChild(nodesource)
    #         root.appendChild(nodesegmented)
    #         root.appendChild(nodesize)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_xmin-i)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_xmax-i)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
            
    #         root.appendChild(nodeobject)


    #         nodeobject = doc.createElement('object')
    #         nodename = doc.createElement('name')
    #         nodename.appendChild(doc.createTextNode("car_half"))  
            
    #         nodetruncated = doc.createElement('truncated')
    #         nodetruncated.appendChild(doc.createTextNode('0'))
    #         nodedifficult = doc.createElement('difficult')
    #         nodedifficult.appendChild(doc.createTextNode('0'))
    #         noderelated   = doc.createElement('extra')
    #         noderelated.appendChild(doc.createTextNode(str(id)))
            
    #         nodebndbox = doc.createElement("bndbox")
    #         nodexmin = doc.createElement("xmin")
    #         nodexmin.appendChild(doc.createTextNode(str(car_half_xmin-i)))
    #         nodeymin = doc.createElement("ymin")
    #         nodeymin.appendChild(doc.createTextNode(str(car_half_ymin)))
    #         nodexmax = doc.createElement("xmax")
    #         nodexmax.appendChild(doc.createTextNode(str(car_half_xmax-i)))
    #         nodeymax = doc.createElement("ymax")
    #         nodeymax.appendChild(doc.createTextNode(str(car_half_ymax)))
            
            
    #         nodeobject.appendChild(nodename)
    #         nodeobject.appendChild(nodetruncated)
    #         nodeobject.appendChild(nodedifficult)
    #         nodeobject.appendChild(noderelated)

    #         nodeobject.appendChild(nodebndbox)
    #         nodebndbox.appendChild(nodexmin)
    #         nodebndbox.appendChild(nodeymin)
    #         nodebndbox.appendChild(nodexmax)
    #         nodebndbox.appendChild(nodeymax)
            
    #         root.appendChild(nodeobject)

    #         if i<int((car_tail_xmax_ori-car_tail_xmin_ori)/2):

    #             nodeobject = doc.createElement('object')
    #             nodename = doc.createElement('name')
    #             nodename.appendChild(doc.createTextNode("car_head"))  
                
    #             nodetruncated = doc.createElement('truncated')
    #             nodetruncated.appendChild(doc.createTextNode('0'))
    #             nodedifficult = doc.createElement('difficult')
    #             nodedifficult.appendChild(doc.createTextNode('0'))
    #             noderelated   = doc.createElement('extra')
    #             noderelated.appendChild(doc.createTextNode(str(id)))
                
    #             nodebndbox = doc.createElement("bndbox")
    #             nodexmin = doc.createElement("xmin")
    #             nodexmin.appendChild(doc.createTextNode(str(car_tail_xmin-i)))
    #             nodeymin = doc.createElement("ymin")
    #             nodeymin.appendChild(doc.createTextNode(str(car_tail_ymin)))
    #             nodexmax = doc.createElement("xmax")
    #             nodexmax.appendChild(doc.createTextNode(str(car_tail_xmax-i)))
    #             nodeymax = doc.createElement("ymax")
    #             nodeymax.appendChild(doc.createTextNode(str(car_tail_ymax)))
                
                
    #             nodeobject.appendChild(nodename)
    #             nodeobject.appendChild(nodetruncated)
    #             nodeobject.appendChild(nodedifficult)
    #             nodeobject.appendChild(noderelated)

    #             nodeobject.appendChild(nodebndbox)
    #             nodebndbox.appendChild(nodexmin)
    #             nodebndbox.appendChild(nodeymin)
    #             nodebndbox.appendChild(nodexmax)
    #             nodebndbox.appendChild(nodeymax)
                
    #             root.appendChild(nodeobject)
    #         fp = open(os.path.join("./save_cut4/"+xml_name.replace(".xml",f"_{i}.xml")), 'w')
    #         doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    #         #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
    #         fp.close()

    # 
    if car and car_tail and car_half and car_tail_xmin_ori-car_xmin_ori>100:
        print("right in") 
        for i in range(1,int((car_xmax_ori-car_xmin_ori)*0.9)): 
            car_xmin=car_xmin_ori
            car_xmax=car_xmax_ori-i
            car_ymin=car_ymin_ori
            car_ymax=car_ymax_ori

            car_half_xmin=car_half_xmin_ori
            car_half_xmax=car_half_xmax_ori-i
            car_half_ymin=car_half_ymin_ori
            car_half_ymax=car_half_ymax_ori

            car_tail_xmin=car_tail_xmin_ori
            car_tail_xmax=car_tail_xmax_ori-i
            car_tail_ymin=car_tail_ymin_ori
            car_tail_ymax=car_tail_ymax_ori

            

            image_cut=image[1:image_h,1:car_xmax] 
            image_name=image_name_origin+f'_-{i}.jpg'
            image_path=os.path.join("./save_cut6/",image_name)
            cv2.imwrite(image_path,image_cut)
            
            doc = xml.dom.minidom.Document()
            root = doc.createElement('annotation')
            doc.appendChild(root) 
        
            nodefoldername = doc.createElement('folder')
            nodefoldername.appendChild(doc.createTextNode(fd))
                
            nodefilename = doc.createElement('filename')
            nodefilename.appendChild(doc.createTextNode(image_name))
                
            nodepath = doc.createElement('path')
            nodepath.appendChild(doc.createTextNode(image_path))
                
            nodesource = doc.createElement('source')
            nodesource.appendChild(doc.createTextNode('Unknown'))
                
            nodesize = doc.createElement('size')
            nodewidth = doc.createElement("width")
            nodewidth.appendChild(doc.createTextNode(str(image_w)))
            nodeheight = doc.createElement("height")
            nodeheight.appendChild(doc.createTextNode(str(image_h)))
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



            nodeobject = doc.createElement('object')
            nodename = doc.createElement('name')
            nodename.appendChild(doc.createTextNode("car"))  
            
            nodetruncated = doc.createElement('truncated')
            nodetruncated.appendChild(doc.createTextNode('0'))
            nodedifficult = doc.createElement('difficult')
            nodedifficult.appendChild(doc.createTextNode('0'))
            noderelated   = doc.createElement('extra')
            noderelated.appendChild(doc.createTextNode(str(id)))
            
            nodebndbox = doc.createElement("bndbox")
            nodexmin = doc.createElement("xmin")
            nodexmin.appendChild(doc.createTextNode(str(car_xmin)))
            nodeymin = doc.createElement("ymin")
            nodeymin.appendChild(doc.createTextNode(str(car_ymin)))
            nodexmax = doc.createElement("xmax")
            nodexmax.appendChild(doc.createTextNode(str(car_xmax-1)))
            nodeymax = doc.createElement("ymax")
            nodeymax.appendChild(doc.createTextNode(str(car_ymax)))
            
            
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

            nodeobject = doc.createElement('object')
            nodename = doc.createElement('name')
            nodename.appendChild(doc.createTextNode("car_half"))  
            
            nodetruncated = doc.createElement('truncated')
            nodetruncated.appendChild(doc.createTextNode('0'))
            nodedifficult = doc.createElement('difficult')
            nodedifficult.appendChild(doc.createTextNode('0'))
            noderelated   = doc.createElement('extra')
            noderelated.appendChild(doc.createTextNode(str(id)))
            
            nodebndbox = doc.createElement("bndbox")
            nodexmin = doc.createElement("xmin")
            nodexmin.appendChild(doc.createTextNode(str(car_half_xmin)))
            nodeymin = doc.createElement("ymin")
            nodeymin.appendChild(doc.createTextNode(str(car_half_ymin)))
            nodexmax = doc.createElement("xmax")
            nodexmax.appendChild(doc.createTextNode(str(car_half_xmax-1)))
            nodeymax = doc.createElement("ymax")
            nodeymax.appendChild(doc.createTextNode(str(car_half_ymax)))
            
            
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

            if i<int((car_tail_xmax_ori-car_tail_xmin_ori)/2):
                nodeobject = doc.createElement('object')
                nodename = doc.createElement('name')
                nodename.appendChild(doc.createTextNode("car_half"))  
                
                nodetruncated = doc.createElement('truncated')
                nodetruncated.appendChild(doc.createTextNode('0'))
                nodedifficult = doc.createElement('difficult')
                nodedifficult.appendChild(doc.createTextNode('0'))
                noderelated   = doc.createElement('extra')
                noderelated.appendChild(doc.createTextNode(str(id)))
                
                nodebndbox = doc.createElement("bndbox")
                nodexmin = doc.createElement("xmin")
                nodexmin.appendChild(doc.createTextNode(str(car_tail_xmin)))
                nodeymin = doc.createElement("ymin")
                nodeymin.appendChild(doc.createTextNode(str(car_tail_ymin)))
                nodexmax = doc.createElement("xmax")
                nodexmax.appendChild(doc.createTextNode(str(car_tail_xmax-1)))
                nodeymax = doc.createElement("ymax")
                nodeymax.appendChild(doc.createTextNode(str(car_tail_ymax)))
                
                
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


            fp = open(os.path.join("./save_cut6/"+xml_name.replace(".xml",f"_-{i}.xml")), 'w')
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
            #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
            fp.close()      










        
        







if __name__=='__main__':
    input_dir='./data'
    # output_dirs=['car','bus','truck']
    # expand_ratio=0.08
    # mk_dir(output_dirs)
    # x=[]
    # y=[]
    # i=0 
    for root,dirs,files in os.walk(input_dir):
        for file in files:
            file_path=os.path.join(root,file)
            f,ext=os.path.splitext(file_path)
            if ext=='.jpg':
                image_path=file_path
                print(image_path)
                read_write_xml(image_path)
                # gen_txt(image_path)
