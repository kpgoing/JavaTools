# coding=utf-8
import os
import sys
import time

ISOTIMEFORMAT = '%Y/%m/%d'


def Tool(rootDir, entityFile, repositoryFile, javaPackage="None", entityNameFlag="Entity",
         respositoryNameFlag="Repository"):
    global respositoryNameDir
    entityNameFlagWithJavaLength = len(entityNameFlag + ".java")
    entityDir = os.path.join(rootDir, entityFile)
    repositoryDir = os.path.join(rootDir, repositoryFile)
    if not os.path.exists(rootDir):
        print rootDir + "不存在!"
    elif not os.path.exists(entityDir):
        print entityDir + "不存在!"
    elif not os.path.exists(repositoryDir):
        print repositoryDir + "不存在!"
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
        for entityName in entityNames:
            try:
                respositoryName = entityName + respositoryNameFlag
                respositoryNameDir = os.path.join(repositoryDir, respositoryName + ".java")
                if os.path.exists(respositoryNameDir):
                    print  respositoryNameDir + "文件已存在,进行跳过处理!"
                else:
                    file = open(respositoryNameDir, "a")
                    file.write("package " + javaPackage + "." + repositoryFile + ";\n"
                                                                                  "import " + javaPackage + "." + entityFile + "." + entityName + entityNameFlag + ";\n"
                                                                                                                                                                   "import org.springframework.data.jpa.repository.JpaRepository;\n"
                                                                                                                                                                   "\n\n"
                                                                                                                                                                   "/**\n"
                                                                                                                                                                   "* 生成于" + time.strftime(
                            ISOTIMEFORMAT, time.localtime()) + "\n"
                                                               "*/\n"
                                                               "public interface " + respositoryName + " extends JpaRepository<" + entityName + entityNameFlag + ",Integer>{\n"
                                                                                                                                                                 "\n}")
                    print respositoryNameDir + "写入成功!"
                    file.close()
            except IOError as err:
                print respositoryNameDir + "写入失败!"


def Choose1():
    Tool(os.getcwd(), sys.argv[1], sys.argv[2])


def Choose2():
    Tool(sys.argv[1], sys.argv[2], sys.argv[3])


def Choose3():
    Tool(os.getcwd(), sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

def Choose4():
    Tool(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

def main():
    chooses = {3: Choose1,
               4: Choose2,
               6: Choose3,
               7: Choose4}
    chooses.get(len(sys.argv))()


Tool("/Users/xubowei/Coding/project/ZCGL2/back/src/main/java/org/cl/zcgl", "entity", "repository","org.cl.zcgl","Entity", "Repository")
# main()
