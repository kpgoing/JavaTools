#使用指南
##本工具并没有太大安全保障，请事先做好代码备份或版本控制。
###JavaRepositoryTool
__根据已经生成的实体生成基础的repository__

1. 命令行执行
	
	|参数序号|描述 |
	| -----|----- |
	|1 |java代码根目录，即entity等java包所在目录,若脚本已在该目录，此参数可省略|
	|2 |实体代码所在包名|
	|3 |repository所在包名，如不存在，会自动创建|
	
	其他若干参数均有默认值，可在代码中查看使用方式
	
###JavaServiceTool
__根据已经生成的实体生成基础的service接口和默认实现(默认放在service下的impl目录下)__

1. 命令行执行
	
	|参数序号|描述 |
	| -----|----- |
	|1 |java代码根目录，即entity等java包所在目录,若脚本已在该目录，此参数可省略|
	|2 |实体代码所在包名|
	|3 |service所在包名，如不存在，会自动创建|
	
	其他若干参数均有默认值，可在代码中查看使用方式
