# coding=utf-8
import os
import sys
import time

ISOTIMEFORMAT = '%Y/%m/%d'


def Tool(rootDir, entityFile, serviceFile, javaPackage="None", entityNameFlag="Entity",
         serviceFlag="Service", serviceImplFlag="Impl", serviceImplDirName="impl"):
    global serviceNameDir
    entityNameFlagWithJavaLength = len(entityNameFlag + ".java")
    entityDir = os.path.join(rootDir, entityFile)
    serviceDir = os.path.join(rootDir, serviceFile)
    if not os.path.exists(rootDir):
        print rootDir + "不存在!"
    elif not os.path.exists(entityDir):
        print entityDir + "不存在!"
    elif not os.path.exists(serviceDir):
        print serviceDir + "不存在!"
    else:
        if javaPackage is "None":
            findPath = os.sep + "main" + os.sep + "java"
            index = rootDir.find(findPath)
            javaPackage = rootDir[index + len(findPath) + 1:]
            javaPackage = javaPackage.replace(os.sep, ".")
            print "java包为: " + javaPackage
        entityNames = []
        for lists in os.listdir(entityDir):
            try:
                if lists.find(entityNameFlag) != -1:
                    entityName = lists[:-(entityNameFlagWithJavaLength)]
                    print "获取实体文件信息" + entityName + "..."
                    entityNames.append(entityName)
            except IOError as err:
                print "获取实体文件信息" + lists + "出错!"
        # 开始创建
        serviceImplDir = os.path.join(serviceDir, serviceImplDirName)
        if not os.path.exists(serviceImplDir):
            os.mkdir(serviceImplDir)
        for entityName in entityNames:
            serviceName = entityName + serviceFlag
            serviceNameDir = os.path.join(serviceDir, serviceName + ".java")
            serviceImplName = serviceName + serviceImplFlag
            serviceImplNameDir = os.path.join(serviceImplDir, serviceImplName + ".java")
            #生成接口
            try:
                if os.path.exists(serviceNameDir):
                    print  serviceNameDir + "文件已存在,进行跳过处理!"
                else:
                    file = open(serviceNameDir, "a")
                    file.write( "package " + javaPackage + "." + serviceFile + ";\n"
                                "import " + javaPackage + "." + entityFile + "." + entityName + entityNameFlag + ";\n"
                                "\n\n"
                                "/**\n"
                                "* 生成于" + time.strftime(ISOTIMEFORMAT, time.localtime()) + "\n"
                                "*/\n"
                                "public interface " + serviceName + " {\n"
                                 "\n}")
                    print serviceNameDir + "写入成功!"
                    file.close()
            except IOError as err:
                print serviceNameDir + "写入失败!"
            #生成实现
            try:
                if os.path.exists(serviceImplNameDir):
                    print  serviceImplNameDir + "文件已存在,进行跳过处理!"
                else:
                    file = open(serviceImplNameDir, "a")
                    file.write( "package " + javaPackage + "." + serviceFile + "." + serviceImplDirName + ";\n"
                                "import " + javaPackage + "." + entityFile + "." + entityName + entityNameFlag + ";\n"
                                "import " + javaPackage + "." + serviceFile + "." + serviceName + ";\n"
                                "\n\n"
                                "/**\n"
                                "* 生成于" + time.strftime(ISOTIMEFORMAT, time.localtime()) + "\n"
                                "*/\n"
                                "@Service\n"
                                "public class " + serviceImplName + " implements " + serviceName + " {\n"
                                 "\n}")
                    print serviceImplNameDir + "写入成功!"
                    file.close()
            except IOError as err:
                print serviceImplNameDir + "写入失败!"

def Choose1():
    Tool(os.getcwd(), sys.argv[1], sys.argv[2])


def Choose2():
    Tool(sys.argv[1], sys.argv[2], sys.argv[3])


def Choose3():
    Tool(os.getcwd(), sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])


def Choose4():
    Tool(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])


def main():
    chooses = {3: Choose1,
               4: Choose2,
               8: Choose3,
               9: Choose4}
    chooses.get(len(sys.argv))()


Tool("/Users/xubowei/Coding/project/ZCGL2/back/src/main/java/org/cl/zcgl", "entity", "service")
# main()
