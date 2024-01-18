D:\python_envs\ML_envs\Scripts\python.exe D:/WorkSpace/workspace/to_sql/cha.py
(function() {
		$(function() {

			var httpstr = "https://user.guancha.cn";// 正式域名 user.guancha.cn
			
			var httpSearchStr='https://s.guancha.cn'//https://s.guancha.cn
			

			function getQueryString(name) {

				var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
				var r = window.location.search.substr(1).match(reg);
				if (r != null) {
					return decodeURI(r[2]); //修改之后
				} else {
					return null;
				}
			}
			sensors.track('search_result', {
				module: "返回搜索结果",
				keyword: getQueryString('keyword'),
			});

			var order = getQueryString('order');
			$("#txtKeyword").val(getQueryString('keyword'))

			var addMore = 'search-news-list';
			var searchUserPage = 1, //搜素用户
				searchTopicPage = 1, //搜索话题
				searchPostPage = 1, //搜索风闻文章
				searchNewsPage = 1, //搜索新闻
				searchSpecialPage = 1, //搜索专题
				searchNewsAuthorPage = 1,
				searchMemberPostPage = 1,
				searchCoursePostPage = 1,
				searchBookPage = 1,
				searchShipingPage = 1,

				isLoadUser = false,
				isLoadTopic = false,
				isLoadPost = false,
				isLoadNews = false,
				isLoadSpecial = false,
				isLoadNewsAuthor = false,
				isLoadMemberPost = false,
				isLoadCoursePost = false,
				isLoadBook = false,
				isLoadShiping = false,

				page = 1;

			var userIds; // 刷新用户关注
			var topicIds; //刷新风闻话题关注







			//ASCII 排序
			function ksort(vm, inputArr, sort_flags) {
				var tmp_arr = {},
					keys = [],
					sorter, i, k, that = vm,
					strictForIn = false,
					populateArr = {};

				switch (sort_flags) {
					case 'SORT_STRING':
						// compare items as strings
						sorter = function(a, b) {
							return that.strnatcmp(a, b);
						};
						break;
					case 'SORT_LOCALE_STRING':
						// compare items as strings, original by the current locale (set with  i18n_loc_set_default() as of PHP6)
						var loc = vm.i18n_loc_get_default();
						sorter = vm.php_js.i18nLocales[loc].sorting;
						break;
					case 'SORT_NUMERIC':
						// compare items numerically
						sorter = function(a, b) {
							return ((a + 0) - (b + 0));
						};
						break;
						// case 'SORT_REGULAR': // compare items normally (don't change types)
					default:
						sorter = function(a, b) {
							var aFloat = parseFloat(a),
								bFloat = parseFloat(b),
								aNumeric = aFloat + '' === a,
								bNumeric = bFloat + '' === b;
							if (aNumeric && bNumeric) {
								return aFloat > bFloat ? 1 : aFloat < bFloat ? -1 : 0;
							} else if (aNumeric && !bNumeric) {
								return 1;
							} else if (!aNumeric && bNumeric) {
								return -1;
							}
							return a > b ? 1 : a < b ? -1 : 0;
						};
						break;
				}

				// Make a list of key names
				for (k in inputArr) {
					if (inputArr.hasOwnProperty(k)) {
						keys.push(k);
					}
				}
				keys.sort(sorter);
				// BEGIN REDUNDANT
				vm.php_js = vm.php_js || {};
				vm.php_js.ini = vm.php_js.ini || {};
				// END REDUNDANT
				strictForIn = vm.php_js.ini['phpjs.strictForIn'] && vm.php_js.ini['phpjs.strictForIn']
					.local_value && vm.php_js
					.ini['phpjs.strictForIn'].local_value !== 'off';
				populateArr = strictForIn ? inputArr : populateArr;

				// Rebuild array with sorted key names
				for (i = 0; i < keys.length; i++) {
					k = keys[i];
					tmp_arr[k] = inputArr[k];
					if (strictForIn) {
						delete inputArr[k];
					}
				}
				for (i in tmp_arr) {
					if (tmp_arr.hasOwnProperty(i)) {
						populateArr[i] = tmp_arr[i];
					}
				}
				return strictForIn || populateArr;
			}

			function getRequestStr(obj) {
				var str = '';
				$.each(obj, function(index, value) {
					if (value) {
						if (str) {
							str += '&' + index + '=' + value;
						} else {
							str += '?' + index + '=' + value;
						}

					}
				});
				return str;
			}




			if (order !== null) {

				if (order == 1) {
					$(".sort-hot").addClass("active");
					$(".sort-time").removeClass("active");
				}
				if (order == 2) {
					$(".sort-time").addClass("active");
					$(".sort-hot").removeClass("active");
				}

			} else {
				order = 1;
			}


			function getList(page) {
				var addrrryyysss = function(data) {
					var ys = 'e10adc3949ba59abbe52313057asd0f883e';
					// data.timestamp =  (new Date()).valueOf();
					requestJson = ksort(this, data, '');
					requestStr = getRequestStr(requestJson);
					requestStr = requestStr.substr(1, requestStr.length);
					//תmd5 + 转大写
					requestStr = encodeURIComponent(requestStr);
					data.gczs = hex_md5(requestStr + ys).toUpperCase();
					return data;
				}
				$(".add-more").hide();
				// $('.add-more').text('正在加载中....');
				var NStr = '';
				var NStr2 = '';
				var NStr3 = '';
				var NStr4 = '';
				var NStr5 = '';
				var NStr6 = '';
				var NStr7 = '';
				var NStr8 = '';
				var NStr9 = '';
				var NStr10 = '';


				// $.ajax({
				// 	url: httpSearchStr + '/main/search-v2',
				// 	type: 'get',
				// 	dataType: 'json',
				// 	xhrFields: {
				// 		withCredentials: true
				// 	},
				// 	data: {
				// 		'page': page,
				// 		'type': addMore,
				// 		'order': order,
				// 		'keyword': $("#txtKeyword").val()

				// 	},
				// 	success: function(res) {
				// 		$('.search-layout').hide();

				// 		if ($.trim(res.data.items) == '') {

				// 			// if (res.data.total_found==page || res.data.total_found==0) {
				// 			$('.add-more').text('没有更多数据了');
				// 			return;
				// 		} else {
				// 			$('.add-more').text('查看更多内容...');
				// 		}


				// 	}
				// });
				// if (addMore == 'search_news_author') {			
				if ($(".search-news-author-tag").hasClass("active")) {

					var data = addrrryyysss({
						'page': page,
						'type': 'search_news_author',
						'order': order,
						'keyword': $("#txtKeyword").val()
					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();

							var dataStr2 = res.data.items;
							for (var i2 = 0; i2 < dataStr2.length; i2++) {
								NStr2 += '<li class="interact-info-box">';
								NStr2 += '<div class="main-info clearfix">';
								NStr2 += '<div class="user-box clearfix">';
								NStr2 += '<div class="user-avatar popup-user news-author-avator">';
								NStr2 += '<a href="' + dataStr2[i2].url +
									'" target="_blank"><img src="' + dataStr2[i2].image +
									'" alt=""></a>';
								NStr2 += '</div>';
								NStr2 += '<div class="user-info-box">';
								NStr2 +=
									'<div class="user-nick"><a  href="' + dataStr2[i2].url +
									'" target="_blank">' +
									dataStr2[i2].name + '</a></div>';
								NStr2 += '<div class="user-introduce"><span>' + dataStr2[i2]
									.description + '</span></div>';
								NStr2 += '</div>';
								NStr2 += '</div>';
								NStr2 += '</div>';
								NStr2 += '</li>';
							}
							$(".search-news-author-list").append(NStr2);
							$(".search-news-author-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							// $(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();

							$(".add-more1").hide();
							$(".add-more2").show();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();

							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more2').text('没有更多数据了');
								return;
							} else {
								$('.add-more2').text('查看更多内容...');
							}



						}
					});

					// } else if (addMore == 'search_post') {
				} else if ($(".search-post-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_post',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr3 = res.data.items;
							//风闻
							for (var i3 = 0; i3 < dataStr3.length; i3++) {
								NStr3 += '<li>';
								NStr3 += '<div class="user-box user-info-box clearfix">';
								NStr3 += '<div class="user-avatar  list-avatar" user-id="' +
									dataStr3[i3].user_id + '">';
								NStr3 += '<img src="' + dataStr3[i3].user_photo + '">';
								NStr3 += '</div>';
								NStr3 += '<div class="user-main list-user-main">';
								NStr3 += '<h4 class="clearfix">';
								// NStr += '<a href="' + dataStr[i].user_description +
								// 	'" target="_blank">' + dataStr[i].user_nick + '</a>';
								NStr3 += '<a href="https://user.' + mylib.getRootDomain() +
									'/user/personal-homepage?uid=' + dataStr3[i3].user_id +
									'"  target="_blank">' + dataStr3[i3].user_nick + '</a>';

								if (dataStr3[i3].user_level_logo != "") {
									NStr3 += '<span class="user-level"><img src="' + dataStr3[i3]
										.user_level_logo + '"></span>';
								} else {
									NStr3 += '<span class="user-level"></span>';
								}

								NStr3 += '<p class="desc">' + dataStr3[i3].user_description +
									'</p>';
								NStr3 += '</h4>';
								NStr3 += '</div>';
								NStr3 += '</div>';
								NStr3 += '<div class="list-item">';
								if (dataStr3[i3].highlight_title) {
									NStr3 += '<h4><a href="https://user.' + mylib.getRootDomain() +
										'/main/content?id=' + dataStr3[i3].id +
										'"  target="_blank">' + dataStr3[i3].highlight_title +
										'</a></h4>';
								} else {
									NStr3 += '<h4><a href="https://user.' + mylib.getRootDomain() +
										'/main/content?id=' + dataStr3[i3].id +
										'"  target="_blank">' + dataStr3[i3].title + '</a></h4>';
								}

								NStr3 += '<div class="item-info">';
								NStr3 += '<div class="item-content">' + dataStr3[i3].summary +
									'</div>';
								NStr3 += '</div>';
								NStr3 += '<div class="clearfix"></div>';
								NStr3 += '</div>';
								NStr3 += '<div class="op-tools">';
								NStr3 += '<ul class="clearfix">';
								NStr3 += '<li>';
								NStr3 += '<a href="javascript:;">点击<span>' + dataStr3[i3]
									.view_count +
									'</span>';
								NStr3 += '</a>';
								NStr3 += '</li>';
								NStr3 += '<li>';
								NStr3 += '<a href="https://user.' + mylib.getRootDomain() +
									'/main/content?id=' + dataStr3[i3].id +
									'&comments-container"  class="comment" data-type="2" data-id="236178" target="_blank">评论 <span>' +
									dataStr3[i3].comment_count + '</span></a>';
								NStr3 += '</li>';
								NStr3 += '<li>';
								NStr3 += '<a >赞 <span>' + dataStr3[i3].praise_num + '</span>';
								NStr3 += '</a>';
								NStr3 += '</li>';
								NStr3 += '<li>';
								if (dataStr3[i3].topics) {

									if (dataStr3[i3].topics[0] != undefined) {
										if (dataStr3[i3].topics[0].topic_name) {
											NStr3 += '<a  href="https://user.' + mylib
												.getRootDomain() +
												'/topic/post-list?topic_id=' + dataStr3[i3].topics[
													0]
												.topic_id +
												'" target="_blank" style="color:#ce3d3a;" class="topic_tag">' +
												dataStr3[i3].topics[0].topic_name + '</a>';
										}
									}

								}
								NStr3 += '</li>';
								NStr3 += '</ul>';
								NStr3 += '<span class="time">' + dataStr3[i3].created_at +
									'</span>';
								NStr3 += '<div class="clear"></div>';
								NStr3 += '</div>';
								NStr3 += '</li>';

							}
							$(".search-post-list").append(NStr3);
							$(".search-post-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							// $(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();

							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").show();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more3').text('没有更多数据了');
								return;
							} else {
								$('.add-more3').text('查看更多内容...');
							}



						}
					});

					// 风闻
					// } else if (addMore == 'search_member_post') {
				} else if ($(".search-member-post-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_member_post',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr4 = res.data.items;
							//观察员文章
							for (var i4 = 0; i4 < dataStr4.length; i4++) {
								NStr4 += '<li>';
								NStr4 += '<div class="user-box user-info-box clearfix">';
								NStr4 +=
									'<div class="user-avatar popup-user list-avatar"><a><img src="' +
									dataStr4[i4].author_photo + '"></a></div>';
								NStr4 +=
									'<div class="user-main list-user-main"><h4 class="clearfix"><a>' +
									dataStr4[i4].column_name + '</a></h4></div></div>';
								NStr4 += '<div class="list-item">';
								NStr4 += '<h4><a href="' + dataStr4[i4].jump_url +
									'" target="_blank">' + dataStr4[i4].title + '</a></h4>';
								NStr4 += '<div class="item-info">';
								if (dataStr4[i4].big_pic) {
									NStr4 += '<div class="item-pic">';
									NStr4 += '<a href="' + dataStr4[i4].jump_url +
										'" target="_blank"><img src="' + dataStr4[i4].big_pic +
										'"></a>';
									NStr4 += '</div>';
								}

								NStr4 += '<div class="item-content">' + dataStr4[i4].summary +
									'</div>';
								NStr4 += '</div>';
								NStr4 += '<div class="clearfix"></div>';
								NStr4 += '</div>';
								NStr4 += '<div class="op-tools">';
								NStr4 += '<ul class="clearfix">';
								NStr4 += '<li>';
								NStr4 += '<a href="' + dataStr4[i4].jump_url +
									'" target="_blank">收藏 <span>' + dataStr4[i4].collection_count +
									'</span>';
								NStr4 += '</a>';
								NStr4 += '</li>';
								NStr4 += '<li>';
								NStr4 += '<a href="' + dataStr4[i4].jump_url +
									'#comment" target="_blank">评论 <span>' + dataStr4[i4]
									.comment_count + '</span>';
								NStr4 += '</a>';
								NStr4 += '</li>';
								NStr4 += '<li>';
								NStr4 += '<a href="' + dataStr4[i4].jump_url +
									'" target="_blank">赞 <span>' + dataStr4[i4].praise_count +
									'</span>';
								NStr4 += '</a>';
								NStr4 += '</li>';
								NStr4 += '<li>';
								if (dataStr4[i4].post_tag) {
									NStr4 += '<a style="color:#ce3d3a;" class="topic_tag" >' +
										dataStr4[i4].post_tag + '</a>';
								}
								NStr4 += '</li>';

								NStr4 += '</ul>';
								NStr4 += '<span class="time">' + dataStr4[i4].format_created_at +
									'</span>';
								NStr4 += '<div class="clear"></div>';
								NStr4 += '</div>';
								NStr4 += '</li>';

							}
							$(".search-member-post-list").append(NStr4);
							$(".search-member-post-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							// $(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();


							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").show();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();

							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more4').text('没有更多数据了');
								return;
							} else {
								$('.add-more4').text('查看更多内容...');
							}



						}
					});

					// 观察员文章
					// } else if (addMore == 'search_user') {
				} else if ($(".search-user-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_user',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr5 = res.data.items;
							//用户
							for (var i5 = 0; i5 < dataStr5.length; i5++) {

								NStr5 += '<li class="interact-info-box">';
								NStr5 += '<div class="main-info clearfix">';
								NStr5 += '<div class="user-box clearfix">';
								NStr5 += '<div class="user-avatar " data-user-id="' + dataStr5[i5]
									.id +
									'">';
								NStr5 += '<img src="' + dataStr5[i5].user_photo +
									'" alt="" style="cursor: pointer;"></div>';

								NStr5 += '<div class="user-info-box">';
								NStr5 += '<div class="user-nick">';
								NStr5 += '<a href="' + dataStr5[i5].home_page +
									'" target="_blank">' +
									dataStr5[i5].user_nick + '</a>';

								if (dataStr5[i5].user_level == 1) {
									NStr5 +=
										'<span class="n_user_v n_user_v_b"><img src="https://user.guancha.cn/static/imgs/lv1-blue.png?2021?asdasd"><span>' +
										dataStr5[i5].bigv_desc + '</span></span>';
								}
								if (dataStr5[i5].user_level == 2) {
									NStr5 +=
										'<span class="n_user_v n_user_v_o"><img src="https://user.guancha.cn/static/imgs/lv2-yellow.png?2021?asdasd"><span>' +
										dataStr5[i5].bigv_desc + '</span></span>';
								}
								if (dataStr5[i5].user_level == 3) {
									NStr5 +=
										'<span class="n_user_v n_user_v_r"><img src="https://user.guancha.cn/static/imgs/lv3-red.png?2021?asdasd"><span>' +
										dataStr5[i5].bigv_desc + '</span></span>';
								}

								// NStr += '<span class="user-level"><img src="' + dataStr[i]
								// 	.user_level_logo + '"></span>';
								NStr5 += '</div>';
								NStr5 +=
									'<div class="user-introduce"><span></span></div>';
								NStr5 += '</div>';
								NStr5 += '</div>';
								NStr5 += '<div class="tools">';
								// if (dataStr[i].has_attention == true) {
								// 	NStr +=
								// 		'<a href="javascript:;" class="attention" data-user-id="' +
								// 		dataStr[i].id + '">已关注</a>';
								// } else {
								NStr5 +=
									'<a href="javascript:;" class="attention" data-user-id="' +
									dataStr5[i5].id + '"><label></label>关注</a>';
								// }

								NStr5 += '<a class="message" href="https://user.' + mylib
									.getRootDomain() + '/user/my-message?to_uid=' + dataStr5[i5]
									.id +
									'"><label></label>私信</a>';
								NStr5 += '</div>';
								NStr5 += '</div>';
								NStr5 += '<ul class="statistics clearfix">';
								NStr5 += '<li>粉丝<span>' + dataStr5[i5].fans_nums + '</span></li>';
								NStr5 += '<li>关注<span>' + dataStr5[i5].attention_nums +
									'</span></li>';
								NStr5 += '<li>文章<span>' + dataStr5[i5].post_nums + '</span></li>';
								NStr5 += '</ul>';
								NStr5 += '</li>';

							}
							$(".search-user-list").append(NStr5);
							$(".search-user-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							// $(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();
							// 用户


							// 刷新用户关注		
							userIds = [];
							$('.search-user-list').find('.user-avatar').each(function() {
								userIds.push($(this).data('user-id'));
							});
							userIds = JSON.stringify(userIds);
							$.ajax({
								url: mylib.getUserUrl() + '/user/get-attention-status',
								type: 'get',
								dataType: 'json',
								xhrFields: {
									withCredentials: true
								},
								data: {
									user_ids: userIds
								},
								success: function(res) {

									if (res.code == 0) {
										data55 = res.data;

										for (var i55 in data55) {
											if (data55[i55] == true) {
												$('.attention[data-user-id=' + i55 +
													']').text('已关注');
											}
										}
									}
								}
							});
							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").show();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();
							// 刷新用户关注
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more5').text('没有更多数据了');
								return;
							} else {
								$('.add-more5').text('查看更多内容...');
							}



						}
					});



					// } else if (addMore == 'search_topic') {
				} else if ($(".search-topic-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_topic',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr6 = res.data.items;
							//风闻话题
							for (var i6 = 0; i6 < dataStr6.length; i6++) {
								NStr6 += '<li class="pt14 pl4">';
								NStr6 += '<div class="topic-box topic-info-box">';
								NStr6 += '<div class="topic-img" >';
								NStr6 += '<img alt="" src="' + dataStr6[i6].topic_img + '">';
								NStr6 += '</div>';
								NStr6 += '<div class="topic-main clearfix">';
								NStr6 += '<h4>';
								NStr6 += '<a href="https://user.' + mylib.getRootDomain() +
									'/topic/post-list?topic_id=' + dataStr6[i6].topic_id + '">' +
									dataStr6[i6].topic_name + '</a>';
								// if (dataStr[i].has_attention == true) {
								// 	NStr +=
								// 		'<a href="javascript:;" class="last follow" data-id="' +
								// 		dataStr[i].topic_id + '">已关注</a>';
								// } else {
								NStr6 +=
									'<a href="javascript:;" class="last follow" data-id="' +
									dataStr6[i6].topic_id + '"><i></i>关注</a>';
								// }

								NStr6 += '</h4>';
								NStr6 += '<ul class="statistics clearfix">';
								NStr6 += '<li><span>' + dataStr6[i6].post_nums + '</span>篇文章</li>';
								NStr6 += '<li><span>' + dataStr6[i6].attention_nums +
									'</span>人关注</li>';
								NStr6 += '</ul>';
								NStr6 += '</div>';
								NStr6 += '<p class="topic-description"></p>';
								NStr6 += '</div>';
								NStr6 += '</li>';
							}
							$(".search-topic-list").append(NStr6);
							$(".search-topic-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							// $(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();
							// 刷新用户关注		
							topicIds = [];
							$('.search-topic-list').find('.follow').each(function() {
								topicIds.push($(this).data('id'));
							});
							topicIds = JSON.stringify(topicIds);
							$.ajax({
								url: mylib.getUserUrl() + '/topic/get-attention-status',
								type: 'get',
								dataType: 'json',
								xhrFields: {
									withCredentials: true
								},
								data: {
									topic_ids: topicIds
								},
								success: function(res) {

									if (res.code == 0) {
										data66 = res.data;

										for (var i66 in data66) {
											if (data66[i66] == true) {
												$('.follow[data-id=' + i66 + ']').text(
													'已关注');
											}
										}
									}
								}
							});
							// 刷新用户关注
							// 风闻话题
							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").show();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more6').text('没有更多数据了');
								return;
							} else {
								$('.add-more6').text('查看更多内容...');
							}



						}
					});

					// } else if (addMore == 'search_special') {
				} else if ($(".search-special-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_special',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();

							var dataStr7 = res.data.items;
							//新闻专题
							for (var i7 = 0; i7 < dataStr7.length; i7++) {
								NStr7 += '<li class="pt14 pl4">';
								NStr7 += '<div class="topic-box topic-info-box">';
								NStr7 += '<div class="topic-img">';
								NStr7 += '<img alt="" src="' + dataStr7[i7].image + '">';
								NStr7 += '</div>';
								NStr7 += '<div class="topic-main clearfix">';
								NStr7 += '<h4 style="padding-top: 10px">';
								NStr7 += '<a href="' + dataStr7[i7].url + '" target="_blank">' +
									dataStr7[i7].name + '</a>';
								NStr7 += '</h4>';
								NStr7 += '</div>';
								NStr7 += '</div>';
								NStr7 += '</li>';

							}
							$(".search-special-list").append(NStr7);
							$(".search-special-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							// $(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();


							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").show();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();

							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more7').text('没有更多数据了');
								return;
							} else {
								$('.add-more7').text('查看更多内容...');
							}


						}
					});

					// 新闻专题
					// } else if (addMore == 'search_course_post') {
				} else if ($(".search-course-post-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_course_post',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr8 = res.data.items;
							//在线课
							for (var i8 = 0; i8 < dataStr8.length; i8++) {


								NStr8 += '<li class="course">';
								NStr8 += '<div class="user-box clearfix">';
								NStr8 += '<div class="user-avatar">';
								NStr8 += '<a >';
								NStr8 += '<img src="' + dataStr8[i8].course_cover + '">';
								NStr8 += '</a>';
								NStr8 += '</div>';
								NStr8 += '<div class="user-main">';
								NStr8 += '<h4 class="clearfix">';
								NStr8 += '<a >在线课</a>';
								NStr8 += '</h4>';
								NStr8 += '</div>';
								NStr8 += '</div>';
								NStr8 += '<div class="content-box clearfix">';
								NStr8 += '<div class="pic">';
								NStr8 += '<a href="' + dataStr8[i8].post_url +
									'" target="_blank">';
								NStr8 += '<img src="' + dataStr8[i8].pic + '">';
								NStr8 += '</a>';
								NStr8 += '</div>';
								NStr8 += '<div class="content-box-right">';
								NStr8 += '<h4>' + dataStr8[i8].course_name + '</h4>';
								NStr8 += '<p>' + dataStr8[i8].title + '</p>';
								NStr8 += '<div class="op-tools">';
								NStr8 += '<ul class="clearfix">';
								NStr8 += '<li>';
								NStr8 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr8[i8].id +
									'" target="_blank">收藏 <span>' + dataStr8[i8].collection_count +
									'</span></a>';
								NStr8 += '</li>';
								NStr8 += '<li>';
								NStr8 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr8[i8].id +
									'&comments-container" target="_blank">评论 <span>' + dataStr8[i8]
									.comment_count + '</span></a>';
								NStr8 += '</li>';
								NStr8 += '<li>';
								NStr8 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr8[i8].id +
									'" target="_blank">赞 <span>' + dataStr8[i8].praise_num +
									'</span></a></li>';
								NStr8 += '</ul>';
								NStr8 += '<span class="time">' + dataStr8[i8].publish_time +
									'</span>';
								NStr8 += '<div class="clear"></div>';
								NStr8 += '</div>';
								NStr8 += '</div>';
								NStr8 += '</div>';
								NStr8 += '</li>';
							}
							$(".search-course-post-list").append(NStr8);
							$(".search-course-post-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							// $(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();

							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").show();
							$(".add-more9").hide();
							$(".add-more10").hide();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more8').text('没有更多数据了');
								return;
							} else {
								$('.add-more8').text('查看更多内容...');
							}



						}
					});


					// 在线课
					// } else if (addMore == 'search_book') {
				} else if ($(".search-book-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_book',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();

							var dataStr9 = res.data.items;
							//观书堂
							for (var i9 = 0; i9 < dataStr9.length; i9++) {
								NStr9 += '<li class="course">';
								NStr9 += '<div class="user-box clearfix">';
								NStr9 += '<div class="user-avatar">';
								NStr9 += '<a>';
								NStr9 += '<img src="' + dataStr9[i9].cover + '">';
								NStr9 += '</a>';
								NStr9 += '</div>';
								NStr9 += '<div class="user-main">';
								NStr9 += '<h4 class="clearfix">';
								NStr9 += '<a>在线课</a>';
								NStr9 += '</h4>';
								NStr9 += '</div>';
								NStr9 += '</div>';
								NStr9 += '<div class="content-box clearfix">';
								NStr9 += '<div class="pic">';
								NStr9 += '<a href="' + dataStr9[i9].post_url +
									'" target="_blank">';
								NStr9 += '<img src="' + dataStr9[i9].banner + '">';
								NStr9 += '</a>';
								NStr9 += '</div>';
								NStr9 += '<div class="content-box-right">';
								NStr9 += '<h4>' + dataStr9[i9].title + '</h4>';
								NStr9 += '<p></p>';
								NStr9 += '<div class="op-tools">';
								NStr9 += '<ul class="clearfix">';
								NStr9 += '<li>';
								NStr9 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr9[i9].id +
									'" target="_blank">收藏 <span>' + dataStr9[i9].collection_count +
									'</span></a>';
								NStr9 += '</li>';
								NStr9 += '<li>';
								NStr9 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr9[i9].id +
									'&comments-container" target="_blank">评论 <span>' + dataStr9[i9]
									.comment_count + '</span></a>';
								NStr9 += '</li>';
								NStr9 += '<li>';
								NStr9 += '<a href="https://member.' + mylib.getRootDomain() +
									'/post/view?id=' + dataStr9[i9].id +
									'" target="_blank">赞 <span>' + dataStr9[i9].praise_num +
									'</span></a></li>';
								NStr9 += '</ul>';
								NStr9 += '<span class="time">' + dataStr9[i9].created_at +
									'</span>';
								NStr9 += '<div class="clear"></div>';
								NStr9 += '</div>';
								NStr9 += '</div>';
								NStr9 += '</div>';
								NStr9 += '</li>';
							}
							$(".search-book-list").append(NStr9);
							$(".search-book-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							// $(".search-book-list").hide();
							$(".search-shiping-list").hide();
							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").show();
							$(".add-more10").hide();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more9').text('没有更多数据了');
								return;
							} else {
								$('.add-more9').text('查看更多内容...');
							}



						}
					});

					// 观书堂
				} else if ($(".search-shiping-tag").hasClass("active")) {
					var data = addrrryyysss({
						'page': page,
						'type': 'search_shiping',
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();

							var dataStr10 = res.data.items;
							//观书堂
							for (var i10 = 0; i10 < dataStr10.length; i10++) {
								NStr10 += '<li>';

								NStr10 += '<div class="list-item">';
								if (dataStr10[i10].highlight_title) {
									NStr10 += '<h4><a href="' + dataStr10[i10].url +
										'" target="_blank">' + dataStr10[i10].highlight_title +
										'</a></h4>';
								} else {
									NStr10 += '<h4><a href="' + dataStr10[i10].url +
										'" target="_blank">' + dataStr10[i10].title + '</a></h4>';
								}
								NStr10 += '<div class="item-info">';
								NStr10 += '<div class="item-content">' + dataStr10[i10].summary +
									'</div>';
								NStr10 += '</div>';
								NStr10 += '<div class="clearfix"></div>';
								NStr10 += '</div>';
								NStr10 += '<div class="op-tools">';
								NStr10 += '<ul class="clearfix">';
								NStr10 += '<li>';
								NStr10 += '<a href="javascript:;">点击<span>' + dataStr10[i10]
									.view_count +
									'</span>';
								NStr10 += '</a>';
								NStr10 += '</li>';
								NStr10 += '<li>';
								NStr10 += '<a href="' + dataStr10[i10].url +
									'#comment" class="comment" data-type="2" data-id="236178" target="_blank">评论 <span>' +
									dataStr10[i10].comment_count + '</span></a>';
								NStr10 += '</li>';
								NStr10 += '<li>';
								if (dataStr10[i10].special) {
									NStr10 += '<a href="' + dataStr10[i10].special_url +
										'" style="color:#ce3d3a;" target="_blank" class="topic_tag">' +
										dataStr10[i10].special + '</a>';
								}
								NStr10 += '</li>';
								NStr10 += '</ul>';
								NStr10 += '<span class="time">' + dataStr10[i10].created_at +
									'</span>';
								NStr10 += '<div class="clear"></div>';
								NStr10 += '</div>';
								NStr10 += '</li>';

							}
							// console.log(NStr10)
							$(".search-shiping-list").append(NStr10);
							$(".search-shiping-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							$(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							// $(".search-shiping-list").hide();
							$(".add-more1").hide();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more10").hide();
							$(".add-more10").show();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more10').text('没有更多数据了');
								return;
							} else {
								$('.add-more10').text('查看更多内容...');
							}



						}
					});

					// 观书堂
				} else {
					var data = addrrryyysss({
						'page': page,
						'type': addMore,
						'order': order,
						'keyword': $("#txtKeyword").val()

					})
				
					$.ajax({
						url: httpSearchStr + '/main/search-v2',
						headers:{'guancha':'search'},
						type: 'get',
						dataType: 'json',
						xhrFields: {
							withCredentials: true
						},
						data: data,
						success: function(res) {
							$('.search-layout').hide();
							var dataStr = res.data.items;
							for (var i = 0; i < dataStr.length; i++) {
								NStr += '<li>';

								NStr += '<div class="list-item">';
								if (dataStr[i].highlight_title) {
									NStr += '<h4><a href="' + dataStr[i].url +
										'" target="_blank">' + dataStr[i].highlight_title +
										'</a></h4>';
								} else {
									NStr += '<h4><a href="' + dataStr[i].url +
										'" target="_blank">' + dataStr[i].title + '</a></h4>';
								}
								NStr += '<div class="item-info">';
								NStr += '<div class="item-content">' + dataStr[i].summary +
									'</div>';
								NStr += '</div>';
								NStr += '<div class="clearfix"></div>';
								NStr += '</div>';
								NStr += '<div class="op-tools">';
								NStr += '<ul class="clearfix">';
								NStr += '<li>';
								NStr += '<a href="javascript:;">点击<span>' + dataStr[i].view_count +
									'</span>';
								NStr += '</a>';
								NStr += '</li>';
								NStr += '<li>';
								NStr += '<a href="' + dataStr[i].url +
									'#comment" class="comment" data-type="2" data-id="236178" target="_blank">评论 <span>' +
									dataStr[i].comment_count + '</span></a>';
								NStr += '</li>';
								NStr += '<li>';
								if (dataStr[i].special) {
									NStr += '<a href="' + dataStr[i].special_url +
										'" style="color:#ce3d3a;" target="_blank" class="topic_tag">' +
										dataStr[i].special + '</a>';
								}
								NStr += '</li>';
								NStr += '</ul>';
								NStr += '<span class="time">' + dataStr[i].created_at + '</span>';
								NStr += '<div class="clear"></div>';
								NStr += '</div>';
								NStr += '</li>';

							}
							$(".search-news-list").append(NStr);
							$(".search-news-list").css({
								'overflow': 'visible',
								'display': 'inline-block'
							});

							// $(".search-news-list").hide();
							$(".search-news-author-list").hide();
							$(".search-post-list").hide();
							$(".search-user-list").hide();
							$(".search-topic-list").hide();
							$(".search-special-list").hide();
							$(".search-member-post-list").hide();
							$(".search-course-post-list").hide();
							$(".search-book-list").hide();
							$(".search-shiping-list").hide();

							$(".add-more1").show();
							$(".add-more2").hide();
							$(".add-more3").hide();
							$(".add-more4").hide();
							$(".add-more5").hide();
							$(".add-more6").hide();
							$(".add-more7").hide();
							$(".add-more8").hide();
							$(".add-more9").hide();
							$(".add-more10").hide();
							if ($.trim(res.data.items) == '') {

								// if (res.data.total_found==page || res.data.total_found==0) {
								$('.add-more1').text('没有更多数据了');
								return;
							} else {
								$('.add-more1').text('查看更多内容...');
							}



						}
					});
					//新闻 默认


					// 新闻
				}
			}



			$(".sort-hot").click(function() {
				$(".sort-time").removeClass("active");
				$(this).addClass("active");
				$(".article-list").empty();
				order = 1;
				page = 1;
				var activeTag = $(".search-control").find(".active")[0].classList[1]
				if (activeTag == "search-book-tag") { //观书堂
					isLoadBook = true;
				} else {
					isLoadBook = false;
				}

				if (activeTag == "search-course-post-tag") { //课程文章
					isLoadCoursePost = true;
				} else {
					isLoadCoursePost = false;
				}


				if (activeTag == "search-member-post-tag") { //会员文章
					isLoadMemberPost = true;
				} else {
					isLoadMemberPost = false;
				}

				if (activeTag == "search-news-author-tag") { //新闻作者
					isLoadNewsAuthor = true;
				} else {
					isLoadNewsAuthor = false;
				}


				if (activeTag == "search-special-tag") { //专题
					isLoadSpecial = true;
				} else {
					isLoadSpecial = false;
				}


				if (activeTag == "search-news-tag") { //新闻
					isLoadNews = true;
				} else {
					isLoadNews = false;
				}


				if (activeTag == "search-topic-tag") { //话题
					isLoadTopic = true;
				} else {
					isLoadTopic = false;
				}

				if (activeTag == "search-user-tag") { //用户
					isLoadUser = true;
				} else {
					isLoadUser = false;
				}

				if (activeTag == "search-post-tag") {
					isLoadPost = true;
				} else {
					isLoadPost = false;
				}

				if (activeTag == "search-shiping-tag") {
					isLoadShiping = true;
				} else {
					isLoadShiping = false;
				}

				getList(page)
			});
			$(".sort-time").click(function() {

				$(".sort-hot").removeClass("active");
				$(this).addClass("active");
				$(".article-list").empty();
				order = 2;
				page = 1;
				var activeTag = $(".search-control").find(".active")[0].classList[1]
				if (activeTag == "search-book-tag") { //观书堂
					isLoadBook = true;
				} else {
					isLoadBook = false;
				}

				if (activeTag == "search-course-post-tag") { //课程文章
					isLoadCoursePost = true;
				} else {
					isLoadCoursePost = false;
				}


				if (activeTag == "search-member-post-tag") { //会员文章
					isLoadMemberPost = true;
				} else {
					isLoadMemberPost = false;
				}

				if (activeTag == "search-news-author-tag") { //新闻作者
					isLoadNewsAuthor = true;
				} else {
					isLoadNewsAuthor = false;
				}


				if (activeTag == "search-special-tag") { //专题
					isLoadSpecial = true;
				} else {
					isLoadSpecial = false;
				}


				if (activeTag == "search-news-tag") { //新闻
					isLoadNews = true;
				} else {
					isLoadNews = false;
				}


				if (activeTag == "search-topic-tag") { //话题
					isLoadTopic = true;
				} else {
					isLoadTopic = false;
				}

				if (activeTag == "search-user-tag") { //用户
					isLoadUser = true;
				} else {
					isLoadUser = false;
				}

				if (activeTag == "search-post-tag") {
					isLoadPost = true;
				} else {
					isLoadPost = false;
				}
				if (activeTag == "search-shiping-tag") {
					isLoadShiping = true;
				} else {
					isLoadShiping = false;
				}
				getList(page)
			});




			$('.search-options').find('input').click(function() {
				var keyword = getQueryString('keyword');
				var order = $(this).val();
				window.location.href = httpSearchStr + '/main/search-v2?click=' + click + '&keyword=' +
					keyword +
					'&order=' + order;
			})

			//加载更多
			$('.add-more').click(function() {

				switch (addMore) {
					case 'search_user':
						searchUserPage++;
						page = searchUserPage;
						break;
					case 'search_topic':
						searchTopicPage++;
						page = searchTopicPage;
						break;
					case 'search_post':
						searchPostPage++;
						page = searchPostPage;
						break;
					case 'search_news':
						searchNewsPage++;
						page = searchNewsPage;
						break;
					case 'search_special':
						searchSpecialPage++;
						page = searchSpecialPage;
						break;
					case 'search_news_author':
						searchNewsAuthorPage++;
						page = searchNewsAuthorPage;
						break;
					case 'search_member_post':
						searchMemberPostPage++;
						page = searchMemberPostPage;
						break;
					case 'search_course_post':
						searchCoursePostPage++;
						page = searchCoursePostPage;
						break;
					case 'search_book':
						searchBookPage++;
						page = searchBookPage;
						break;
					case 'search_shiping':
						searchShipingPage++;
						page = searchShipingPage;
						break;
				}
				getList(page);
			});

			function resetStatus(obj, addmore, showDiv) {

				$(obj).siblings('a').removeClass('active');
				$(obj).addClass('active');
				// $('.add-more').text('查看更多内容...');
				addMore = addmore;
				if (typeof showDiv != 'undefined') {
					$('.' + showDiv).show();
					$('.' + showDiv).siblings('ul').hide();
					$(obj).parent('ul').show();
				}
			}

			//点击风闻
			$('.search-control').on('click', '.search-post-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").show();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'post';
				resetStatus(this, 'search_post', 'search-post-list');
				// $('.search-relate').show();
				$('.search-post-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadPost) {
					getList(1);
					isLoadPost = true;
					page = 1;
				}
				// getList(1);
			});

			//点击用户
			$('.search-control').on('click', '.search-user-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").show();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'user';
				resetStatus(this, 'search_user', 'search-user-list');
				$('.search-user-list').parent().removeClass('index-list').addClass('box-left');
				if (!isLoadUser) {
					getList(1);
					isLoadUser = true;
					page = 1;
				}
				// getList(1);
			});


			//点击话题
			$('.search-control').on('click', '.search-topic-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").show();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'topic';
				resetStatus(this, 'search_topic', 'search-topic-list');
				$('.search-topic-list').parent().removeClass('index-list').addClass('box-left');
				if (!isLoadTopic) {
					getList(1);
					isLoadTopic = true;
					page = 1;
				}
				// getList(1);
			});

			//点击新闻
			$('.search-control').on('click', '.search-news-tag', function(event) {
				$(".add-more1").show();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				// console.log(isLoadNews)
				click = 'news';
				resetStatus(this, 'search_news', 'search-news-list');
				$('.search-news-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadNews) {
					getList(1);
					isLoadNews = true;
					page = 1;
				}
				// getList(1);
			});

			//点击专题
			$('.search-control').on('click', '.search-special-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").show();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'special';
				resetStatus(this, 'search_special', 'search-special-list');
				$('.search-special-list').parent().removeClass('index-list').addClass('box-left');
				if (!isLoadSpecial) {
					getList(1);
					isLoadSpecial = true;
					page = 1;
				}
				// getList(1);
			});
			//点击新闻作者
			$('.search-control').on('click', '.search-news-author-tag', function(event) {

				$(".add-more1").hide();
				$(".add-more2").show();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'news-author';
				resetStatus(this, 'search_news_author', 'search-news-author-list');
				$('.search-special-list').parent().removeClass('index-list').addClass('box-left');
				if (!isLoadNewsAuthor) {
					getList(1);
					isLoadNewsAuthor = true;
					page = 1;
				}
				// getList(1);
			});
			//点击会员文章
			$('.search-control').on('click', '.search-member-post-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").show();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'member-post';
				resetStatus(this, 'search_member_post', 'search-member-post-list');
				$('.search-member-post-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadMemberPost) {
					getList(1);
					isLoadMemberPost = true;
					page = 1;
				}
				// getList(1);
			});

			//点击课程文章
			$('.search-control').on('click', '.search-course-post-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").show();
				$(".add-more9").hide();
				$(".add-more10").hide();
				click = 'course-post';
				resetStatus(this, 'search_course_post', 'search-course-post-list');
				$('.search-course-post-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadCoursePost) {

					getList(1);
					isLoadCoursePost = true;
					page = 1;
				}
				// getList(1);
			});

			//点击观书堂
			$('.search-control').on('click', '.search-book-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").show();
				$(".add-more10").hide();
				click = 'book';
				resetStatus(this, 'search_book', 'search-book-list');
				$('.search-book-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadBook) {

					getList(1);
					isLoadBook = true;
					page = 1;
				}
				// getList(1);
			});

			//点击时评
			$('.search-control').on('click', '.search-shiping-tag', function(event) {
				$(".add-more1").hide();
				$(".add-more2").hide();
				$(".add-more3").hide();
				$(".add-more4").hide();
				$(".add-more5").hide();
				$(".add-more6").hide();
				$(".add-more7").hide();
				$(".add-more8").hide();
				$(".add-more9").hide();
				$(".add-more10").show();
				click = 'shiping';
				resetStatus(this, 'search_shiping', 'search-shiping-list');
				$('.search-shiping-list').parent().removeClass('box-left').addClass('index-list');
				$('.index-list').css({
					'width': 810
				});
				if (!isLoadShiping) {

					getList(1);
					isLoadShiping = true;
					page = 1;
				}
				// getList(1);
			});

			//点击相关用户的更多
			$('.to-search-user').click(function() {
				$('.search-control').find('.search-user-tag').click();
			});
			//点击相关话题的更多
			$('.to-search-topic').click(function() {
				$('.search-control').find('.search-topic-tag').click();
			});
			//点击相关新闻的更多
			$('.to-search-news').click(function() {
				$('.search-control').find('.search-news-tag').click();
			});
			//点击相关新闻作者的更多
			$('.to-search-news-author').click(function() {
				$('.search-control').find('.search-news-author-tag').click();
			});
			//默认点击


			var click = getQueryString('click');

			if (typeof click != 'undefined') {
				switch (click) {
					case 'news':
						$('.search-control').find('.search-news-tag').click();
						break;
					case 'post':
						$('.search-control').find('.search-post-tag').click();
						break;
					case 'topic':
						$('.search-control').find('.search-topic-tag').click();
						break;
					case 'special':
						$('.search-control').find('.search-special-tag').click();
						break;
					case 'user':
						$('.search-control').find('.search-user-tag').click();
						break;
					case 'news-author':
						$('.search-control').find('.search-news-author-tag').click();
						break;
					case 'member-post':
						$('.search-control').find('.search-member-post-tag').click();
						break;
					case 'course-post':
						$('.search-control').find('.search-course-post-tag').click();
						break;
					case 'book':
						$('.search-control').find('.search-book-tag').click();
						break;
					case 'shiping':
						$('.search-control').find('.search-shiping-tag').click();
						break;
					default:
						$('.search-control').find('.search-news-tag').click();
				}

			} else {
				$('.search-control').find('.search-news-tag').click();
			}
			//点击收藏
			var opTools = $('.article-list').find('.op-tools');
			var collectButtons = $('.article-list').find('.op-tools').find('a').eq(2); //收藏
			var praiseButtons = $('.article-list').find('.op-tools').find('a').eq(4); //赞

			//绑定点击收藏事件
			// $('.article-list').on('click', '.collection', function(event) {
			//     var postId = $(this).attr('data-id');
			//     mylib.collect(postId, this);
			//     return false;
			// });

			function interact(actionType, obj) {
				var number = parseInt($(obj).find('span').text());
				if (isNaN(number)) {
					number = 0;
				}
				if (actionType == 'cancel') {
					number--;
					if (number <= 0) {
						number = '';
					}

					$(obj).find('span').text(number);
					$(obj).removeClass('active');
				} else {
					number++;

					$(obj).find('span').text(number);

					$(obj).addClass('active');
				}
			}
			//绑定点击收藏事件
			$('.article-list').on('click', '.collection', function(event) {
				//文章的收藏
				var codeType = $(this).attr('data-type');
				var codeId = $(this).attr('data-id');
				var obj = this;
				if (!mylib.checkLogin()) return;
				$.ajax({
					url: '/post/collect',
					type: 'GET',
					dataType: 'jsonp',
					data: {
						'codeId': codeId,
						'codeType': codeType
					},
					success: function(res) {
						if (res.code == 0) {
							interact(res.data.action, obj);
						}
					}
				});

			});

			//关注
			$('.search-user-list').on('click', '.attention', function(event) {

				var that = this;
				var uid = $(this).attr('data-user-id');

				mylib.sendPostAjax('https://user.' + mylib.getRootDomain() + '/user/attention', {
					to_user_id: uid
				}, function(res) {
					if (res.code == 0) {
						if (res.data.action == 'cancel') {
							$(that).html('<label></label>关注');

						} else {
							$(that).text('已关注');
							// 刷新用户关注
							var userIdsPush = [];

							userIdsPush.push(uid);
							userIdsPush = JSON.stringify(userIdsPush);
							// $.ajax({
							// 	url: mylib.getUserUrl() + '/user/get-attention-status',
							// 	type: 'get',
							// 	dataType: 'json',
							// 	xhrFields: {
							// 		withCredentials: true
							// 	},
							// 	data: {
							// 		user_ids: userIdsPush
							// 	},
							// 	success: function(res) {
							// 		if (res.code = 0) {
							// 			data = res.data;


							// 		}
							// 	}
							// });

						}
					}
				});



			});
			//关注话题
			$('.search-topic-list').on('click', '.follow', function() {
				var that = this;
				var id = $(this).attr('data-id');
				mylib.sendPostAjax('https://user.' + mylib.getRootDomain() + '/topic/follow', {
					topic_id: id
				}, function(res) {
					if (res.code == 0) {
						if (res.data.action == 'set') {
							$(that).html('已关注');
							$(that).addClass('active');
							//$(that).unbind('click');
							//$(that).removeAttr("href");
							//$(that).removeAttr("data-id");
							// 刷新风闻话题关注
							var topicIdsPush = [];

							topicIdsPush.push(id);
							topicIdsPush = JSON.stringify(topicIdsPush);
							$.ajax({
								url: mylib.getUserUrl() +
									'/topic/get-attention-status',
								type: 'get',
								dataType: 'json',
								xhrFields: {
									withCredentials: true
								},
								data: {
									topic_ids: topicIdsPush
								},
								success: function(res) {
									if (res.code = 0) {
										data = res.data;


									}
								}
							});

						} else if (res.data.action == 'cancel') {
							$(that).html('<i></i>关注');
							$(that).removeClass('active');
						}
					}
				});
				return false;
			});

			//当只有一个列表的时候
			if ($('.search-relate-list').find('li').length == 1) {
				$('.search-relate-list').find('.name').each(function() {
					$(this).css({
						'overflow': 'visible',
						'display': 'inline-block'
					});
				});
			}

			//搜索模块

			function buildSearchList(data) {
				if (data.length <= 0) {
					return '';
				}
				var list = '';
				for (var i in data) {
					var index = parseInt(i) + 1;
					list += '<li data-keyword="' + data[i].keyword + '"><span class="num top' + index +
						'">' +
						index + '</span>' + data[i].keyword + '</li>';
				}
				return list;
			}
			// $('.search-input2').find('input').focus(function(event) {
			// 	//获取数据
			// 	//拼出页面
			// 	$.ajax({
			// 		url: httpstr + '/main/get-hot-keyword',
			// 		type: 'get',
			// 		dataType: 'json',
			// 		success: function(res) {
			// 			if (res.code == 0) {
			// 				var list = buildSearchList(res.data);
			// 				$('.search-layout').find('.hot-search-list').html(list);
			// 				$('.search-layout').show();
			// 			}
			// 		},
			// 	});

			// });
			$('.search-input2').click(function(event) {
				event.stopPropagation();
			});

			$('#txtKeyword').focus(function() {
				var searchHistoryData = mylib.getCookie('search-history');
				if (searchHistoryData == null) {
					searchHistory = [];
				} else {
					searchHistory = JSON.parse(searchHistoryData);
					//从cookie中提取出关键字插入到搜索下拉列表中
					var str = '';
					for (var i = 0; i < searchHistory.length; i++) {
						str += '<li data-keyword="' + searchHistory[i] + '">' + searchHistory[i] +
							'<span class="del">x</span></li>';
					}
					$('.history-search-list').append(str);
					//添加删除事件
					$('.history-search-list').find('.del').click(function() {
						var keyword = $(this).parent().data('keyword');
						for (var i = 0; i < searchHistory.length; i++) {
							if (searchHistory[i] == keyword) {

								searchHistory.splice(i, 1);
								break;
							}
						}
						//写会cookie
						searchHistoryData = JSON.stringify(searchHistory);
						mylib.setCookie('search-history', searchHistoryData);
						$(this).parent().remove();

						return false;
					});
				}
			})

			//鼠标划过
			$('.search-input2').on('mouseover', '.search-layout li', function() {

				$(this).siblings().removeClass('active');
				$(this).addClass('active');
			});

			//点击关键词开始搜索
			$('.search-input2').on('click', '.search-layout li', function() {

				var keyword = $(this).data('keyword');
				$('.search-input2').find('input').val(keyword);
				$('#searchBtn').click();
				$('.search-layout').hide();

				//return false;
			});
			//将html转换成实体
			function convert(str) {
				var entitys = {
					'&': '&amp;',
					'<': '&lt;',
					'>': '&gt;',
					'"': '&quot;',
					"'": '&apos;'
				};
				var regexp = new RegExp('[' + Object.keys(entitys).join('') + ']', 'g');
				// console.log(str)
				return str.replace(regexp, function(matched) {
					return entitys[matched];
				});
			}
			//点击搜索栏里面的放大镜进行搜索
			$('.search-input2').find('a').click(function() {

				page = 1;
				var activeTag = $(".search-control").find(".active")[0].classList[1]
				if (activeTag == "search-book-tag") { //观书堂
					isLoadBook = true;
				} else {
					isLoadBook = false;
				}

				if (activeTag == "search-course-post-tag") { //课程文章
					isLoadCoursePost = true;
				} else {
					isLoadCoursePost = false;
				}


				if (activeTag == "search-member-post-tag") { //会员文章
					isLoadMemberPost = true;
				} else {
					isLoadMemberPost = false;
				}

				if (activeTag == "search-news-author-tag") { //新闻作者
					isLoadNewsAuthor = true;
				} else {
					isLoadNewsAuthor = false;
				}


				if (activeTag == "search-special-tag") { //专题
					isLoadSpecial = true;
				} else {
					isLoadSpecial = false;
				}


				if (activeTag == "search-news-tag") { //新闻
					isLoadNews = true;
				} else {
					isLoadNews = false;
				}


				if (activeTag == "search-topic-tag") { //话题
					isLoadTopic = true;
				} else {
					isLoadTopic = false;
				}

				if (activeTag == "search-user-tag") { //用户
					isLoadUser = true;
				} else {
					isLoadUser = false;
				}

				if (activeTag == "search-post-tag") {
					isLoadPost = true;
				} else {
					isLoadPost = false;
				}

				if (activeTag == "search-shiping-tag") {
					isLoadShiping = true;
				} else {
					isLoadShiping = false;
				}
				// var url = 'https://user.' + mylib.getRootDomain() + '/main/search';
				var url = window.location.pathname
				var keyword = $("#txtKeyword").val();
				keyword = convert(keyword);
				if ($.trim(keyword) != '') {
					//将关键词记录进cookie

					if ($.isArray(searchHistory)) {
						if (searchHistory.indexOf(keyword) == -1) {
							//console.log('aaa');
							searchHistory.unshift(keyword);
							if (searchHistory.length > 5) {
								searchHistory.pop();
							}
						} else {
							//删除在头部重新添加
							searchHistory.splice(searchHistory.indexOf(keyword), 1);
							searchHistory.unshift(keyword);
						}
						searchHistoryData = JSON.stringify(searchHistory);
						mylib.setCookie('search-history', searchHistoryData);
					}

					keyword = encodeURIComponent(keyword);

					$(".article-list").empty();
					getList(1)
					sensorsSearchResult();

				} else {
					mylib.msg('搜索内容不能为空');
				}

			});
			//点击搜索栏进行搜索
			$('#searchBtn').click(function() {

				page = 1;
				var activeTag = $(".search-control").find(".active")[0].classList[1]
				if (activeTag == "search-book-tag") { //观书堂
					isLoadBook = true;
				} else {
					isLoadBook = false;
				}

				if (activeTag == "search-course-post-tag") { //课程文章
					isLoadCoursePost = true;
				} else {
					isLoadCoursePost = false;
				}


				if (activeTag == "search-member-post-tag") { //会员文章
					isLoadMemberPost = true;
				} else {
					isLoadMemberPost = false;
				}

				if (activeTag == "search-news-author-tag") { //新闻作者
					isLoadNewsAuthor = true;
				} else {
					isLoadNewsAuthor = false;
				}


				if (activeTag == "search-special-tag") { //专题
					isLoadSpecial = true;
				} else {
					isLoadSpecial = false;
				}


				if (activeTag == "search-news-tag") { //新闻
					isLoadNews = true;
				} else {
					isLoadNews = false;
				}


				if (activeTag == "search-topic-tag") { //话题
					isLoadTopic = true;
				} else {
					isLoadTopic = false;
				}

				if (activeTag == "search-user-tag") { //用户
					isLoadUser = true;
				} else {
					isLoadUser = false;
				}

				if (activeTag == "search-post-tag") {
					isLoadPost = true;
				} else {
					isLoadPost = false;
				}

				if (activeTag == "search-shiping-tag") {
					isLoadShiping = true;
				} else {
					isLoadShiping = false;
				}

				var url = 'https://user.' + mylib.getRootDomain() + '/main/search';
				var keyword = $("#txtKeyword").val();
				keyword = convert(keyword);
				if ($.trim(keyword) != '') {
					//将关键词记录进cookie

					if ($.isArray(searchHistory)) {
						if (searchHistory.indexOf(keyword) == -1) {
							//console.log('aaa');
							searchHistory.unshift(keyword);
							if (searchHistory.length > 5) {
								searchHistory.pop();
							}
						} else {
							//删除在头部重新添加
							searchHistory.splice(searchHistory.indexOf(keyword), 1);
							searchHistory.unshift(keyword);
						}
						searchHistoryData = JSON.stringify(searchHistory);
						mylib.setCookie('search-history', searchHistoryData);
					}

					keyword = encodeURIComponent(keyword);

					$(".article-list").empty();
					getList(1)
					sensorsSearchResult();



				} else {
					mylib.msg('搜索内容不能为空');
				}

			});
			//按回车提交搜索
			$(document).keydown(function(e) {


				page = 1;
				var activeTag = $(".search-control").find(".active")[0].classList[1]
				if (activeTag == "search-book-tag") { //观书堂
					isLoadBook = true;
				} else {
					isLoadBook = false;
				}

				if (activeTag == "search-course-post-tag") { //课程文章
					isLoadCoursePost = true;
				} else {
					isLoadCoursePost = false;
				}


				if (activeTag == "search-member-post-tag") { //会员文章
					isLoadMemberPost = true;
				} else {
					isLoadMemberPost = false;
				}

				if (activeTag == "search-news-author-tag") { //新闻作者
					isLoadNewsAuthor = true;
				} else {
					isLoadNewsAuthor = false;
				}


				if (activeTag == "search-special-tag") { //专题
					isLoadSpecial = true;
				} else {
					isLoadSpecial = false;
				}


				if (activeTag == "search-news-tag") { //新闻
					isLoadNews = true;
				} else {
					isLoadNews = false;
				}


				if (activeTag == "search-topic-tag") { //话题
					isLoadTopic = true;
				} else {
					isLoadTopic = false;
				}

				if (activeTag == "search-user-tag") { //用户
					isLoadUser = true;
				} else {
					isLoadUser = false;
				}

				if (activeTag == "search-post-tag") {
					isLoadPost = true;
				} else {
					isLoadPost = false;
				}

				if (activeTag == "search-shiping-tag") {
					isLoadShiping = true;
				} else {
					isLoadShiping = false;
				}
				if (e.which === 13) {
					var searchInput = $('.search-input2').find('input');
					var val = searchInput.val();
					if (searchInput.is(':focus') && $.trim(val) != '') {
						$(".article-list").empty();
						getList(1)
						sensorsSearchResult();

						// $('.search-input2').find('a').click();
						return false;
					}

				}
			});
		});
	})();



	// 返回搜索结果
	function sensorsSearchResult() {
		sensors.track('search_result', {
			// module:"返回搜索结果",
			keyword: $("#txtKeyword").val(),
		});
	}



	//按ESC关闭提出框
	$(document).keydown(function(e) {
		if (e.which === 27) {
			mylib.closePopup();
		}
	});

Process finished with exit code 0
