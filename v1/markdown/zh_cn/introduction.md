#简介

[Amy Brown](http://aosabook.org/en/intro1.html#brown-amyOD)和[Greg Wilson](http://aosabook.org/en/intro1.html#wilson-greg)

木工是一门难学的手艺，人们可以花费毕生的精力学习如何做到上乘水准。但是，木工不是架构：如果我们从间距板和斜接缝之中抽身出来看，建筑从总体上是需要设计的，而怎么做设计就像手艺或科学一样，也是一门艺术。

编程也是一门难学的手艺，人们也可以花费毕生精力学习如何编程。但是编程不是软件架构。许多程序员花费数年时间思考更大的设计难题或与它们做斗争：这个应用应该具备可扩展性吗？如果需要具备，那么是通过提供脚本接口，通过某种插件机制，还是通过其他完全不同的方式呢？客户端需要做什么，服务器端需要做什么，而且，“客户端－服务器”的模式适合这个应用吗？这些不是编程的问题，这些问题要比木工活里往哪儿放楼梯的问题要更大一些。

建筑架构和软件架构有很多相通的地方，但也有一个重要的区别。在培训中或在他们的职业生涯里，建筑架构师研究了数以千计的建筑，然而大部分软件开发者只对一部分大型程序有所了解。而且通常情况下，那些程序是他们自己写的。他们从来没有了解过历史上伟大的程序，也没有阅读过经验丰富的实践者对于那些程序设计的评论。结果就是，他们重复着别人的错误，而不是在别人成功的基础上构建软件。

这本书的目的就是为了改变这种现状。书的每一章都描绘了一个开源应用软件的架构：它是怎么组织的，它的各个部分是如何交互的，为什么要用那种方式构建，以及我们从中能学到什么经验，以便应用到其他大型的设计问题。这些描述都是由对软件非常了解的人写的，这些人都有数年甚至数十年的设计和重构应用软件的经验。这些应用软件取材较广，从简单的绘画程序、基于网页的样式表程序到编译器小工具和数百万行代码的可视化工具包都有。有些软件诞生不过几年，有些却已经接近30周年了。它们的共同点是这些软件作者都对设计做了长时间的、深刻的思考，而且他们愿意分享他们的想法。希望读者能喜欢他们所写的内容。

##贡献者

Eric P. Allman (Sendmail)：Eric Allman是sendmail, syslog和trek的作者，以及Sendmail公司的联合创始人。他在“开源软件”这个名字还没诞生时就已经开始写开源软件了，更别提之后的“开源运动”了。他是美国计算机协会（ACM）队列编辑审查委员会的一员，也是计算性能理事会的成员之一。他的个人网站是：[http://www.neophilic.com/~eric](http://www.neophilic.com/~eric)。

Keith Bostic (Berkeley DB)：Keith曾是加州大学伯克利分校计算机系统研究小组的成员之一，在那儿他做过2.10BSD版本的架构师，也做过4.4BSD以及相关版本的主要开发者。他获得了USENIX终生成就奖（“火焰奖”）<sup>1</sup>，这个奖项是为了表彰他在Unix社区非凡的贡献，他还获得了加州大学伯克利分校的卓越成就奖，以表彰他推动了4BSD版本的开源。Keith是开源嵌入式数据库系统Berkeley DB的架构师和最初的开发者之一。

Amy Brown (编辑)：Amy拥有滑铁卢大学数学系学士学位，并且从事软件行业已达10年之久。现在她写书并且从事编辑工作，有时也写写软件。她和两个孩子以及一只非常老的猫住在多伦多。

C\. Titus Brown (持续集成)：Titus在演进式建模、物理气象学、发展生物学、基因组学和生物信息学领域都工作过。他现在是密歇根州立大学的助理教授，在那里他的兴趣拓展到一些新的领域，包括科学软件的再生性和可维护性。他同时也是Python软件基金会（Python Software Foundation）的成员，他的博客地址是：[http://ivory.idyll.org](http://ivory.idyll.org)。

Roy Bryant (Snowflock)：在20年里作为软件架构师和首席技术官（CTO），Roy设计的系统包括电子工作台（现在是国家仪器仿真软件）和Linkwalker数据管道，这个系统曾在2006年凭借高性能计算获得了微软的全球成功客户大奖。在卖掉他最后的一个创业公司之后，他返回到多伦多大学开始上计算机科学的研究生，研究方向是虚拟化和云计算。最近，在2011年，Roy在ACM的欧洲系统大会（ACM's Eurosys Conference）上发布了他在Snowflock上做的Kaleidoscope扩展包。他的个人网站是：[http://www.roybryant.net/](http://www.roybryant.net/)。

Russell Bryant (Asterisk)：Russell是Digium公司开源软件团队的工程经理。从2004年秋天开始他成为Asterisk开发团队的核心成员。从那以后，他对Asterisk开发的几乎每个领域都有所贡献，从项目管理到核心架构设计和开发。他的博客地址是：[http://www.russellbryant.net](http://www.russellbryant.net)。

Rosangela Canino-Koning (持续集成)：在经过了13年软件行业的摸爬滚打之后，Rosangela返回大学读取密歇根州立大学计算机科学和进化生物学的博士学位。她在大量的闲暇时间里，喜欢阅读、徒步、旅行和鼓捣开源生物信息软件。她的博客地址是：[http://www.voidptr.net](http://www.voidptr.net)。

Francesco Cesarini (Riak)：Francesco Cesarini从1995年开始就一直用Erlang语言在爱立信开发各种不同的整包项目（turnkey projects），包括OTP R1版本。他是Erlang Solutions<sup>2</sup>的创始人，同时也是O'Reilly出版的《Erlang编程》的合著者。 他现在是Erlang Solutions的技术总监，同时他也抽空会在英国的牛津大学、瑞典的哥德堡信息技术大学教本科生和研究生等。

Robert Chansler (HDFS<sup>3</sup>)：Robert是雅虎公司软件研发高级经理。从卡内基梅隆大学分布式系统专业研究生毕业之后，他做过编译器（Tartan Labs），打印和成像系统（Adobe Systems），电子商务（Adobe Systems，Impresse）以及存储区域网络管理（SanNavigator, McDATA）。回到分布式系统和HDFS之后，Rob发现很多相似的问题，但是数据量多了两个或三个以上的零。

James Crook (Audacity)：James是来自爱尔兰都柏林的合同软件开发者。目前他在为电子设计制作工具，再之前的话他开发过生物信息软件。他对Audacity有很多大胆的计划，他希望至少其中的一部分计划能够面世。

Chris Davis (Graphite)：Chris是一位软件顾问和谷歌工程师，他已经在设计和构建可伸缩的监控和自动化工具上面工作超过12年。Chris于2006年开始写Graphite，从那之后就开始领导这个开源项目。在不写代码时，他喜欢厨艺、制作音乐或者做点研究。他的研究兴趣包括知识建模、群论、信息论、混沌理论和复杂系统。

Juliana Freire (VisTrails)：Juliana是犹他大学计算机科学系的助理教授。在此之前，她是贝尔实验室（朗讯科技）数据库系统研究部门技术人员，也曾是OGI/OHSU的助理教授。她的研究兴趣包括溯源<sup>4</sup>、科学数据管理、信息整合以及Web挖掘<sup>5</sup>。 她是美国国家科学基金职业奖和IBM学院奖获得者。她的研究由美国国家科学基金会、美国能源部、美国国立卫生研究院、IBM、微软和雅虎提供资金支持。

Berk Geveci (VTK)：Berk是Kitware公司科学计算的总监。他负责领导Paraview的研发工作，Paraview是一个获奖的基于VTK的可视化应用。他的研究兴趣包括大规模并行计算、计算动力学、有限元和可视化算法。

Andy Gross (Riak)：Andy Gross是Basho技术公司的首席架构师，管理Basho的开源和企业版数据存储系统的设计和开发。Andy于2007年加入Basho，当时他已经有10年的软件和分布式系统工程经验。在Basho之前，Andy在Mochi Media、苹果公司和Akamai技术公司担任分布式系统高级工程师。

Bill Hoffman (CMake): Bill是Kitware公司的首席技术官（CTO）<sup>6</sup>和联合创始人。 他是CMake项目的主要开发者，而且他有超过20年大规模C++系统的工作经验。

Cay Horstmann (Violet)：Cay是圣何塞州立大学计算机科学的教授，但是他经常离开校园做一些业内工作或者是在其他国家教书。他是很多编程语言和软件设计书籍的作者，他也是Violet和GridWorld开源程序的原始作者。

Emil Ivov (Jitsi)：Emil是Jitsi项目（之前的SIP Communicator）的创始人和项目带头人。他也参与其他的一些项目例如ice4j.org和JAIN SIP项目。Emil于2008年初获得斯特拉斯堡大学的博士学位，从那以后他就主要专注于Jitsi相关的活动。

David Koop (VisTrails)：David是犹他大学计算机系的在读博士生（2011年夏天毕业）。他的研究兴趣包括可视化、溯源和科学数据管理。他是VisTrails系统的开发主管，也是VisTrails公司的高级软件架构师。

Hairong Kuang (HDFS)是Hadoop项目的长期贡献者和提交者，她对于Hadoop的工作充满热情。她现在在Facebook工作，之前在雅虎工作。在进入这个行业之前，她曾是加利福尼亚州立工艺大学波莫纳分校的助理教授。她在加州大学欧文分校获得计算机博士学位。她的兴趣包括云计算、移动代理<sup>7</sup>、并行计算和分布式系统。

H\. Andrés Lagar-Cavilla (Snowflock): Andrés是一位软件系统研究员，他主要从事虚拟化、操作系统、安全、集群计算和移动计算方面的实验工作。他有阿根廷的应用科学学士学位，同时拥有多伦多大学计算机科学的硕士和博士学位。他的个人网站是：[http://lagarcavilla.org](http://lagarcavilla.org)。

Chris Lattner (LLVM)：Chris是一位软件开发者，他有各种各样的兴趣和经验，特别是在编译器工具链、操作系统和图像渲染领域。他是开源项目LLVM的设计者和首席架构师。关于Chris和他的项目的更多信息可以参见：[http://nondot.org/~sabre/](http://nondot.org/~sabre/) 。

Alan Laudicina (Thousand Parsec)：Alan是韦恩州立大学计算机科学的在读研究生，他所学的专业是分布式计算。在业务时间他喜欢写代码，学习编程语言和玩扑克。关于他的更多信息可以参见：[http://alanp.ca/](http://alanp.ca/)。

Danielle Madeley (Telepathy): Danielle是澳大利亚的软件工程师，她在Collabora有限公司从事感应和其他一些神奇的工作。她取得了电子工程和计算机科学的双学位。她同时也收藏了大量的毛绒企鹅。她的博客地址是：[http://blogs.gnome.org/danni/](http://blogs.gnome.org/danni/)。
	
Adam Marcus (NoSQL)：Adam是麻省理工学院计算机科学和人工智能实验室的博士生，主要研究方向是数据库系统和社交计算的交叉领域。他最新的工作是把传统的数据库系统绑定到社交媒体流入如Twitter和人类计算平台例如Mechanical Turk。他喜欢在他的研究原型之上构建有用的开源系统，更喜欢深入了解开源存储系统。他的博客地址是：[http://blog.marcua.net](http://blog.marcua.net)。

Kenneth Martin (CMake)：Ken现在是Kitware公司的主席和首席财务官，Kitware是一个位于美国的研发公司。Ken在1998年联合创立了Kitware，然后通过努力使得公司发展到现在的地位，Kitware现在是拥有许多政府和商业领域客户的研发供应商领导者。 

Aaron Mavrinac (Thousand Parsec)：Aaron是温莎大学电子和计算机工程系的在读博士生，研究方向是摄影机网络、计算机视觉和机器人。在闲暇时间，他会忙活Thousand Parsec和其他一些自由软件，他用Python和C语言写程序，同时为了用好这两门语言也做了很多其他方面的工作。他的网站地址是：[http://www.mavrinac.com](http://www.mavrinac.com)。

Kim Moir (Eclipse)：Kim在渥太华IBM Rational软件研究所工作，她承担Eclipse和Runtime Equinox项目的版本工程负责人的角色，同时她也是Eclipse架构委员会的成员。她的兴趣包括构建优化、Equinox和创建基于组件的软件。工作之余，她喜欢和小伙伴们一起跑步，准备下一次的公路赛。她的博客地址是：[http://relengofthenerds.blogspot.com/](http://relengofthenerds.blogspot.com/)。

Dirkjan Ochtman (Mercurial)：Dirkjan于2010年作为计算机科学研究生毕业，已经在一个财务创业公司工作了3年。业余时间除了休闲之外，他会折腾Mercurial、Python、Gentoo Linux和Python的CouchDB库。他居住在美丽的城市阿姆斯特丹。他的个人网站是：[http://dirkjan.ochtman.nl/](http://dirkjan.ochtman.nl/)。

Sanjay Radia (HDFS)：Sanjay是雅虎公司Hadoop项目的架构师，也是Apache软件基金会（Apache Software Foundation）Hadoop的提交者以及项目管理委员会委员。在此之前他做过Cassatt、Sun和INTRIA公司的高级工程师，主要的工作是开发分布式系统和格/效用计算基础框架的软件。Sanjay拥有加拿大滑铁卢大学计算机科学博士学位。

Chet Ramey (Bash)：Chet参与bash项目已经超过20年，过去的17年都是bash的主要开发者。他是俄亥俄州克利夫兰市凯斯西储大学的长期员工，他也在这所大学取得了学士和硕士学位。他和家人以及宠物居住在克利夫兰附近。他的个人主页是：[http://tiswww.cwru.edu/~chet](http://tiswww.cwru.edu/~chet)。

Emanuele Santos (VisTrails)：Emanuele是犹他大学的研究科学家。她的研究兴趣包括科学数据管理、可视化和溯源。她于2010年获得了犹他大学计算系的博士学位。她也是VisTrails系统的开发负责人。

Carlos Scheidegger (VisTrails)：Carlos拥有犹他大学的计算博士学位，现在在AT&T研究所做研究员。Carlos于2007年获得了IEEE可视化的最佳论文奖，并于2008年获得了国际图形建模会议（Shape Modeling International）最佳论文奖。他的研究兴趣包括数据可视化和分析、几何处理和计算机图形学。

Will Schroeder (VTK)：Will是Kitware公司的总裁和联合创始人。他是经过培训的计算科学家，而且是VTK的关键开发者之一。他喜欢写漂亮的代码，特别是和计算几何学或图形学相关的部分。

Margo Seltzer (Berkeley DB)：Margos是哈佛工程和应用科学学校计算机科学[Herchel Smith](http://en.wikipedia.org/wiki/Herchel_Smith)讲席教授，也是Oracle公司的架构师。她曾是Berkeley DB的主要设计师，也曾是Sleepycat软件公司的联合创始人。她的研究兴趣是文件系统、数据库系统、交易系统和医疗数据挖掘。她的专业生活网页地址在：[http://www.eecs.harvard.edu/~margo](http://www.eecs.harvard.edu/~margo)，她自己的博客地址是：[http://mis-misinformation.blogspot.com/](http://mis-misinformation.blogspot.com/)。

Justin Sheehy (Riak)：Justin是Basho技术公司的首席技术官，Basho就是打造Webmachine和Riak背后的公司。在Basho之前，他曾是MITRE公司的首席科学家和Akamai系统基础架构的高级架构师。在这两个公司，他专注于高可靠分布式系统的多个方面，包括调度算法、基于语言的范式模型和高弹性的研究。

Richard Shimooka (Battle for Wesnoth)：Richard是安大略省金斯敦皇后大学防御管理研究项目的研究助理。他也是Battle for Wesnoth的副管理员和秘书长。Richard写过几部著作，洞察了从政府到开源项目的社会群组的组织文化。

Konstantin V. Shvachko (HDFS)：Konstantin是HDFS开发的老兵，也是eBay公司Hadoop项目首席架构师。Konstantin擅长大规模分布式存储系统的高效数据结构和算法。他发现了一种新的平衡树，叫做S树，可以用作非结构化数据的最佳索引，他也曾是基于S树的Linux文件系统treeFS（reiserFS原型）的主要开发者。Konstantin拥有俄罗斯莫斯科国立大学计算机科学博士学位。他也是Apache Hadoop项目管理委员会的成员。

Claudio Silva (VisTrails)：Claudio是犹他大学计算机科学系的全职教授。他的研究兴趣有可视化、几何计算、计算机图形学和科学数据管理。1996年，他在纽约州立大学石溪分校取得了计算机科学博士学位。2011年下半年，他会加入纽约大学理工学院任职计算机科学和工程系的全职教授。

Suresh Srinivas (HDFS)：Suresh是雅虎公司HDFS项目的软件架构师。他是Hadoop的提交者，也是Apache软件基金会的项目管理委员会委员。在来到雅虎之前，他在Sylantro系统公司开发可伸缩的托管通信服务的基础架构。Suresh拥有印度卡纳塔克邦技术研究所电子和通信专业的学士学位。

Simon Stewart (Selenium)：Simon居住在伦敦，是谷歌测试部门的一名软件工程师。他是Selenium项目的核心贡献者，也是WebDriver的创始人，他对开源非常有热情。Simon喜欢喝啤酒，也喜欢写漂亮的软件，有时同时进行。他的个人主页是：[http://www.pubbitch.org/](http://www.pubbitch.org/)。

Audrey Tang (SocialCalc)：Audrey是一位台湾自学成才的程序员和译者。她现在在Socialtext工作，职位抬头是”无标题页“（Untitled Page），同时也是苹果公司本地化和版本工程的合同工。在此之前，她设计并领导过Pugs项目，第一个可以工作的Perl 6的实现；她也曾经在多个语言（Haskell，Perl 5和Perl 6）设计委员会供职，她对CPAN和Hackage也作出过大量贡献。她的博客地址是：[http://pugs.blogs.com/audreyt/](http://pugs.blogs.com/audreyt/)。

Huy T. Vo (VisTrails)：Huy将于2011年5月获得犹他大学的博士学位。他的研究兴趣包括可视化、数据流架构和科学数据管理。他是VisTrails公司的高级开发者。他也同时任职纽约大学理工学院的研究助理教授。

David White (Battle for Wesnoth)：David是Battle for Wesnoth的创始人和开发负责人。David曾经做过几个开源的视频游戏项目，包括他联合创立的Frogatto。David是旅游科技领导者Sabre控股的性能工程师。 

Greg Wilson (editorial)：Greg在高性能科学计算、数据可视化和计算机安全领域已经工作超过25年，他是多本计算机书籍包括2008年获得Jolt大奖的Beautiful Code）和两本儿童读物的作者或编辑。Greg在1993年取得了爱丁堡大学计算机科学博士学位。他的博客地址是：[http://third-bit.com](http://third-bit.com)和[http://software-carpentry.org](http://software-carpentry.org)。

Tarek Ziadé (Python Packaging)：Tarek居住在法国的勃艮第。他是Mozilla公司的高级软件工程师，使用Python语言构建服务器。在业余时间，他领导Python的packaging工作。

##鸣谢

非常感谢我们的评审者：

|                   |                             |                       |
| :---------------- | :-------------------------- |:--------------------- |
| Eric Aderhold     | Muhammad Ali                | Lillian Angel         |
| Robert Beghian    | Taavi Burns                 | Luis Pedro Coelho     |
| David Cooper      | Mauricio de Simone          | Jonathan Deber        |
| Patrick Dubroy    | Igor Foox                   | Alecia Fowler         |
| Marcus Hanwell    | Johan Harjono               | Vivek Lakshmanan      |
| Greg Lapouchnian  | Laurie MacDougall Sookraj   | Josh McCarthy         |
| Jason Montojo     | Colin Morris                | Christian Muise       |
| Victor Ng         | Nikita Pchelin              | Andrew Petersen       |
| Andrey Petrov     | Tom Plaskon                 | Pascal Rapicault      |
| Todd Ritchie      | Samar Sabie                 | Misa Sakamoto         |
| David Scannell    | Clara Severino              | Tim Smith             |
| Kyle Spaans       | Sana Tapal                  | Tony Targonski        |
| Miles Thibault    | David Wright                | Tina Yee              |


我们同时非常感谢Jackie Carter，他帮助我们做了早期的编辑工作。

封面图片来自Peter Dutton的摄影，取自Chris Denison的作品，位于缅因州波特兰市的48 Free Street的壁画。本图片按照[Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic license](http://creativecommons.org/licenses/by-nc-sa)协议授权。

##献辞

<div align="center">献给Brian Kernighan，他教会了我们太多东西，也献给世界各地的政治犯。</div>

###译者注
1. Flame Award参见[usenix官方介绍](https://www.usenix.org/about/flame)和[维基百科的说明](http://zh.wikipedia.org/wiki/USENIX)。
2. Erlang Solutions的官方网站：[https://www.erlang-solutions.com/](https://www.erlang-solutions.com/)。
3. HDFS代表Hadoop分布式文件系统，具体参见 [http://zh.wikipedia.org/wiki/Apache_Hadoop](http://zh.wikipedia.org/wiki/Apache_Hadoop)。
4. 溯源，原词是provenance，在科学技术领域，可以参考维基百科的解释：h[ttp://en.wikipedia.org/wiki/Provenance#Science](ttp://en.wikipedia.org/wiki/Provenance#Science)
5. Web挖掘（Web mining）：数据挖掘技术的一种应用，目标是从web上发现模式。根据分析的目标，web挖掘可以分为三种不同的类型，即Web使用挖掘、Web内容挖掘和Web结构挖掘。具体参见 [http://en.wikipedia.org/wiki/Web_mining](http://en.wikipedia.org/wiki/Web_mining)。
6. 本书中technical director翻译成技术总监，而CTO翻译成首席技术官。
7. 移动代理：mobile agents，在计算机科学中，移动代理就是计算机软件和数据的组合，它能够自动地从一台计算机迁移（或移动）到另一台计算机，并且能在目标计算机上继续执行。具体参见：[http://en.wikipedia.org/wiki/Mobile_agent](http://en.wikipedia.org/wiki/Mobile_agent)。
