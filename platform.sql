-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: localhost:8889
-- Generation Time: 2015-06-17 08:34:32
-- 服务器版本： 5.5.34
-- PHP Version: 5.5.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `platform`
--

-- --------------------------------------------------------

--
-- 表的结构 `article`
--

CREATE TABLE `article` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `atitle` varchar(100) NOT NULL DEFAULT '',
  `acontent` text,
  `acreatetime` datetime DEFAULT NULL,
  `amodifytime` datetime DEFAULT NULL,
  `acid` int(11) NOT NULL,
  `acheck` tinyint(1) DEFAULT '0',
  `abc` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`aid`),
  KEY `FK_ID` (`acid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- 转存表中的数据 `article`
--

INSERT INTO `article` (`aid`, `atitle`, `acontent`, `acreatetime`, `amodifytime`, `acid`, `acheck`, `abc`) VALUES
(1, '综合指数', '<p>青春再见最后一班午夜列车　　</p><p>悄悄带走了青春　　</p><p>最亲爱的人最美的时光</p><p>渐渐刺痛了回忆　　</p><p>留不住什么换不回什么　　</p><p>青春终究要散场　　</p><p>我得到什么我失去什么　　</p><p>生命终究要告别　　</p><p>青春再见吧那放肆的幸福　　</p><p>青春再见吧那无尽的忧伤　　</p><p>在这一瞬间感觉如此靠近　　</p><p>在这一瞬间却又如此遥远　　</p><p>留不住什么换不回什么　　</p><p>青春终究要散场　　</p><p>我得到什么我失去什么　　</p><p>生命终究要告别　　</p><p>青春再见吧那放肆的幸福　　</p><p>青春再见吧那无尽的忧伤　　</p><p>在这一瞬间感觉如此靠近　　</p><p>在这一瞬间却又如此遥远　　</p><p>啊青春再见啊青春再见　　</p><p>啊青春再见吧再见吧再见吧　　</p><p>如果一天 我就要离去　　</p><p>请把我留在回忆里</p>', '2015-06-02 00:00:00', '2015-06-04 23:28:19', 1, 1, 0),
(3, '先行指数', '<p>借我那把枪吧</p><p>你说你用不上那玩意去杀谁</p><p>莫非有人把情爱都已看厌</p><p>借我那把枪吧</p><p>或者借我五毛钱</p><p>我要搭上北方的快车 头也不回</p><p>杀了诚实吧</p><p>或者杀了爱情吧</p><p>在北风吹起的时侯加入我们的队伍</p><p>杀了真理吧</p><p>或者杀了谎言吧</p><p>好在北风吹起的狂野中</p><p>唱着激昂的进行曲</p><p>借我那把枪吧</p><p>我又没说用不上那玩意</p><p>莫非有人给你机会</p><p>让你感到自卑</p><p>借我那把枪吧</p><p>或者借我五毛钱</p><p>生就属于北方的我将一去不回</p><p>如果有天我再归来</p><p>请不要因为我感到伤悲</p><p>雁子会捎来讯息</p><p>当春风吹拂着新绿</p><p>那是因为我想你</p><p>跟我去北方吧</p><p>那里正下着雪</p><p>就让我滚热的灵魂在冰霜上撒个野</p><p>跟我去北方吧</p><p>逃离爱情的肤浅</p><p>南方的江山太娇媚</p><p>腐蚀了我的热血</p><p>杀了诚实吧 或者杀了爱情吧</p><p>爱情来的时侯</p><p>你就会背叛你的诚实主义</p><p>杀了真理吧 或者杀了谎言吧</p><p>千万不要让他们站在敌对的那一边</p><p>借我那把枪吧</p><p>我又没说用不上那玩意儿</p><p>当真理站在谎言的那边</p><p>我就解决我自己</p><p>借我那把枪吧</p><p>或者借我五毛钱</p><p>南方的江山太娇媚</p><p>容易遮上我的眼</p><p>如果有天我再回来</p><p>请不要为我感到伤悲</p><p>雁子会捎来讯息</p><p>当春风吹拂着新绿</p><p>那是因为我想你</p>', '2015-06-04 13:28:17', '2015-06-04 23:29:50', 1, 1, 0),
(5, '一致指数', '<p>当你老了 头发白了</p><p>睡意昏沉</p><p>当你老了 走不动了</p><p>炉火旁取暖 回忆青春</p><p>多少人曾爱你青春欢畅的时辰</p><p>爱慕你的美丽 假意或真心</p><p>只有一个人还爱你虔诚的灵魂</p><p>爱你苍老的脸上的皱纹</p><p>当你老了 眼眉低垂</p><p>灯火昏黄不定</p><p>风吹过来 你的消息</p><p>这就是我心里的歌</p><p>多少人曾爱你青春欢畅的时辰</p><p>爱慕你的美丽 假意或真心</p><p>只有一个人还爱你虔诚的灵魂</p><p>爱你苍老的脸上的皱纹</p><p>我留不住所有的岁月</p><p>岁月却留住我</p><p>不曾为我停留的芬芳</p><p>却是我的春天</p><p>多少人曾爱你青春欢畅的时辰</p><p>爱慕你的美丽 假意或真心</p><p>只有一个人还爱你虔诚的灵魂</p><p>爱你苍老的脸上的皱纹</p><p>当你老了 眼眉低垂</p><p>灯火昏黄不定</p><p>风吹过来 你的消息</p><p>这就是我心里的歌</p><p>当我老了 我要为你</p><p>唱起这首心里的歌</p><p>唱起这首心里的歌</p>', '2015-06-04 23:30:45', '2015-06-15 10:37:53', 5, 1, 0),
(6, '六大行业指数', '<p>窗外那片娇艳的花丛。</p><p>就像记忆中闪亮的瞬间，</p><p>墙上那片婆娑的暗影。</p><p>唤起我心中无限的思念，</p><p>你从这离开的那一天。</p><p>我才知道你就是春天，</p><p>此刻春天已悄悄地流走。</p><p>留给我心中无尽的思念，</p><p>我不知道你是否美丽依然。</p><p>我不知道你是否还会回来，</p><p>有一天你再飞过这儿的天空。</p><p>请你停下在我寂寞的窗台，</p><p>远处那片金黄的麦田。</p><p>就像梦中你我的乐园，</p><p>桌上那张发黄的相片。</p><p>唤起我心中无尽的思念，</p><p>我终于失去你的那一天。</p><p>我才明白你就是永远，</p><p>永远就会慢慢地破碎。</p><p>留下的是不变的思念，</p><p>我不知道你是否美丽依然。</p>', '2015-06-04 23:31:21', '2015-06-17 10:07:28', 3, 1, 1),
(7, '评价方法', '<p>青春彷佛因我爱你开始</p><p>但却令我看破爱这个字</p><p>自你患上失忆</p><p>便是我扭转命数的事</p><p>只因当失忆症发作加深</p><p>没记住我但却另有更新蜜运</p><p>像狐狸精般 并未允许我步近</p><p>无回忆的余生 忘掉往日情人</p><p>却又记住移情别爱的命运</p><p>无回忆的男人 就当偷厄与瞒骗</p><p>抱抱我不过份</p><p>吻下来 豁出去</p><p>这吻别似覆水</p><p>再来也许要天上团聚</p><p>再回头 你不许</p><p>如曾经不登对</p><p>你何以双眼好像流泪</p><p>彼此追忆不怕爱要终止</p><p>但我大概上世做过太多坏事</p><p>能从头开始 跪在教堂说愿意</p><p>娱乐行的人影 还在继续繁荣</p><p>我在算着甜言蜜语的寿命</p><p>人造的蠢卫星 没探测出我们已</p><p>已再见不再认</p><p>Repeat</p><p>吻下来 豁出去</p><p>这吻别似覆水</p><p>再来也许要天上团聚</p><p>我下来 你出去</p><p>讲再会也心虚</p><p>我还记得到天上团聚</p><p>吻下来 豁出去</p><p>从前多么登对</p><p>你何以双眼好像流泪</p><p>每年这天记得再流泪</p>', '2015-06-04 23:33:50', '2015-06-04 23:33:50', 2, 1, 0),
(8, '评价结果', '<p>我胆小地对自己说 就是这样吗</p><p>我是你眼里的太阳 也是你影子里的悲伤</p><p>我问我 这世界是否一如往常</p><p>让我照耀你 安息的时光</p><p>你是我 小心维护的梦</p><p>我疲倦地享受着 谁也无法代替的光芒</p><p>我是我 一碰就碎的太阳</p><p>我热切地希望 能在消失之前得到信仰</p><p>我胆小地对自己说 就是这样吗</p><p>我是你眼里的太阳 也是你影子里的骄傲</p><p>我问我 这世界是否一如往常</p><p>需要我在拥挤午夜发光</p><p>你是我 小心维护的梦</p><p>我疲倦地享受着 谁也无法代替的孤傲</p><p>我是我 疲倦流浪的太阳</p><p>我热切地希望 能在消失之前得到信仰</p><p>你是我小心维护的梦</p><p>我疲倦地享受着 谁也无法靠近的孤傲</p><p>我是我 疲倦流浪的太阳</p><p>无法为自己 无法为谁停止下来</p><p>我是我 一碰就碎的太阳</p><p>我热切地希望 能在消失之前</p><p>得到得到 得到信仰</p>', '2015-06-04 23:34:48', '2015-06-15 10:37:45', 4, 1, 0),
(9, '最新进展', '<p>我确实说 我这样说 我不在乎结果</p><p>我对你说 我有把握 成功例子好多</p><p>人们虚假又造作 总爱得不温不火</p><p>我们用真心就不会有差错</p><p>我没想过我会难过 你竟然离开我</p><p>爱沿着抛物线 离幸福 总降落得差一点</p><p>流着血心跳却不曾被心痛削灭 真真切切</p><p>青春的抛物线 把未来始于相遇的地点</p><p>至高后才了解 世上月圆月缺只是错觉</p><p>我好想说 我只想说 我不要这后果</p><p>可是你说 相对来说 走开是种解脱</p><p>当初亲密的动作 变成当下的闪躲</p><p>感情的过程出了什么差错</p><p>我没想过我会难过 你终于离开我</p><p>爱沿着抛物线 离幸福 总降落得差一点</p><p>流着血心跳却不曾被心痛削灭 真真切切</p><p>青春的抛物线 把未来始于相遇的地点</p><p>至高后才了解 世上月圆月缺只是错觉</p><p>爱沿着抛物线 离幸福 总降落得差一点</p><p>流着血心跳却不曾被心痛削灭 真真切切</p><p>青春的抛物线 把未来始于相遇的地点</p><p>至高后才了解 世上月圆月缺只是错觉</p><p>至高后才了解 世上月圆月缺只是错觉</p>', '2015-06-04 23:35:16', '2015-06-04 23:35:55', 2, 1, 0);

-- --------------------------------------------------------

--
-- 表的结构 `category`
--

CREATE TABLE `category` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) NOT NULL DEFAULT '',
  `ccheck` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 转存表中的数据 `category`
--

INSERT INTO `category` (`cid`, `cname`, `ccheck`) VALUES
(1, '上市公司景气指数', 1),
(2, '上市公司质量评价', 1),
(3, 'Media Zone', 1),
(4, 'Science', 1),
(5, 'Publish', 1);

-- --------------------------------------------------------

--
-- 表的结构 `links`
--

CREATE TABLE `links` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `ltitle` varchar(100) NOT NULL DEFAULT '',
  `lurl` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `links`
--

INSERT INTO `links` (`lid`, `ltitle`, `lurl`) VALUES
(1, 'Github', 'http://www.github.com');

-- --------------------------------------------------------

--
-- 表的结构 `setting`
--

CREATE TABLE `setting` (
  `sname` varchar(100) NOT NULL DEFAULT '',
  `sadmin` varchar(100) NOT NULL DEFAULT '',
  `spwd` varchar(100) NOT NULL DEFAULT '',
  `scount` bigint(20) NOT NULL DEFAULT '0',
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `setting`
--

INSERT INTO `setting` (`sname`, `sadmin`, `spwd`, `scount`, `sid`) VALUES
('Company', 'wangchen', 'd4224c42dffa50efe85544c28f0c2e1c', 1176, 1);

--
-- 限制导出的表
--

--
-- 限制表 `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `FK_ID` FOREIGN KEY (`acid`) REFERENCES `category` (`cid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
