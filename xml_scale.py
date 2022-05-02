from configparser import Interpolation
from tkinter import Scale
import cv2
import os
# import xml.etree.ElementTree as ET
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
    # scale=0.5
    for scale in range(1,15):
        scale=round(scale*0.1,1)
        fd,image_name=os.path.split(image_path)
        xml_name=image_name.replace(".jpg",".xml")
        xml_name="./save/"+xml_name
        image=cv2.imread(image_path)
        if image is not None:
            scale_image_h=int(image.shape[0]*scale)
            scale_image_w=int(image.shape[1]*scale)
            scale_image=cv2.resize(image,(scale_image_w,scale_image_h),interpolation=cv2.INTER_AREA)
            cv2.imshow("save",scale_image)
            cv2.waitKey(0)
            cv2.imwrite(os.path.join("./save",image_name.replace(".jpg",f"_{str(scale)}.jpg")),scale_image)
    #####read_xml#########
        xml_path=image_path.replace(".jpg",".xml")
        tree=ET.parse(xml_path)
        root_read=tree.getroot()

    ######write_xml#########
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
        nodewidth.appendChild(doc.createTextNode(str(scale_image_w)))
        nodeheight = doc.createElement("height")
        nodeheight.appendChild(doc.createTextNode(str(scale_image_h)))
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
        for obj in root_read.iter('object'):
            bbox=get_bbox_xyxy(obj)
            vehicle_class=bbox[0]
            xmin=bbox[1]*scale
            ymin=bbox[2]*scale
            xmax=bbox[3]*scale
            ymax=bbox[4]*scale
            id  =bbox[5]
            nodeobject = doc.createElement('object')
            
            nodename = doc.createElement('name')
            nodename.appendChild(doc.createTextNode(vehicle_class))  
            
            nodetruncated = doc.createElement('truncated')
            nodetruncated.appendChild(doc.createTextNode('0'))
            nodedifficult = doc.createElement('difficult')
            nodedifficult.appendChild(doc.createTextNode('0'))
            noderelated   = doc.createElement('extra')
            noderelated.appendChild(doc.createTextNode(str(id)))
            
            nodebndbox = doc.createElement("bndbox")
            nodexmin = doc.createElement("xmin")
            nodexmin.appendChild(doc.createTextNode(str(xmin)))
            nodeymin = doc.createElement("ymin")
            nodeymin.appendChild(doc.createTextNode(str(ymin)))
            nodexmax = doc.createElement("xmax")
            nodexmax.appendChild(doc.createTextNode(str(xmax)))
            nodeymax = doc.createElement("ymax")
            nodeymax.appendChild(doc.createTextNode(str(ymax)))
            
            
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
        fp = open(xml_name.replace(".xml",f"_{scale}.xml"), 'w')
        doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        #doc.writexml(fp, indent='\t', addindent='\t', newl='\n')
        fp.close()









# def gen_txt(image_path):
#     xml_path=image_path.replace(".png",".xml")
#     txt_path=image_path.replace(".png",".txt")
#     root,image_name=os.path.split(image_path)
#     tree=ET.parse(xml_path)
#     root=tree.getroot()
#     image=cv2.imread(image_path)
#     if image is not None:
#         image_h=image.shape[0]
#         image_w=image.shape[1]
#         # obj_num=0
#         with open(txt_path,'w') as f:
#             for obj in root.iter('object'):
#                 if obj is not None:
#                     bbox=get_bbox_xyxy(obj)
#                     vehicle_class=bbox[0]
#                     vehicle_class=convert_label(vehicle_class)
#                     xmin=bbox[1]
#                     ymin=bbox[2]
#                     xmax=bbox[3]
#                     ymax=bbox[4]
#                     x_center=(xmin+xmax)/2
#                     y_center=(ymin+ymax)/2
#                     box_w=xmax-xmin
#                     box_h=ymax-ymin
#                     x_center_new=x_center*1.0/image_w
#                     y_center_new=y_center*1.0/image_h
#                     box_w_new=box_w/image_w
#                     box_h_new=box_h/image_h
#                     # print(vehicle_class,x_center_new,y_center_new,box_w_new,box_h_new,"\n")
#                     f.write(str(vehicle_class)+" "+str(x_center_new)+" "+str(y_center_new)+" "+str(box_w_new)+" "+str(box_h_new)+"\n")



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
